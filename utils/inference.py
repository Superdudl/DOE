import sys

sys.path.append(__file__)
import tensorrt as trt
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit

TRT_LOGGER = trt.Logger(trt.Logger.INFO)
builder = trt.Builder(TRT_LOGGER)


with open('NAFNet.trt', "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
    engine = runtime.deserialize_cuda_engine(f.read())

context = engine.create_execution_context()

input_size = context.get_tensor_shape(engine.get_tensor_name(0))
output_size = context.get_tensor_shape(engine.get_tensor_name(1))

d_input = cuda.mem_alloc(trt.volume(input_size) * trt.float32.itemsize)
d_output = cuda.mem_alloc(trt.volume(input_size) * trt.float32.itemsize)

output = cuda.pagelocked_empty(tuple(output_size), dtype=np.float32)

stream = cuda.Stream()

input = np.random.rand(*tuple(input_size)).astype(np.float32)
cuda.memcpy_htod_async(d_input, input, stream)

bindings = [int(d_input), int(d_output)]

for i in range(engine.num_io_tensors):
            context.set_tensor_address(engine.get_tensor_name(i), bindings[i])

context.execute_async_v3(stream_handle=stream.handle)
stream.synchronize()
cuda.memcpy_dtoh_async(output, d_output, stream)
stream.synchronize()
pass