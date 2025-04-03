import sys

sys.path.append(__file__)
import tensorrt as trt
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit


class Inference:

    def create(self, model):
        self.model = model
        TRT_LOGGER = trt.Logger(trt.Logger.INFO)

        with open(self.model, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
            self.engine = runtime.deserialize_cuda_engine(f.read())

        self.context = self.engine.create_execution_context()
        self.input_size = self.context.get_tensor_shape(self.engine.get_tensor_name(0))
        self.output_size = self.context.get_tensor_shape(self.engine.get_tensor_name(1))

        self.d_input = cuda.mem_alloc(trt.volume(self.input_size) * trt.float32.itemsize)
        self.d_output = cuda.mem_alloc(trt.volume(self.input_size) * trt.float32.itemsize)

        self.output = cuda.pagelocked_empty(tuple(self.output_size), dtype=np.float32)
        self.stream = cuda.Stream()
        self.bindings = [int(self.d_input), int(self.d_output)]

        for i in range(self.engine.num_io_tensors):
            self.context.set_tensor_address(self.engine.get_tensor_name(i), self.bindings[i])

    def __call_(self, input: np.uint8):
        input = np.float32(input / 255).transpose(2, 0, 1)
        cuda.memcpy_htod_async(self.d_input, input, self.stream)
        self.context.execute_async_v3(stream_handle=self.stream.handle)
        self.stream.synchronize()
        cuda.memcpy_dtoh_async(self.output, self.d_output, self.stream)
        self.stream.synchronize()
        return self.output
