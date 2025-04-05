import sys

sys.path.append(__file__)
import tensorrt as trt
import numpy as np
import pycuda.driver as cuda
import time


class Inference:
    def __init__(self, /):
        super().__init__()
        cuda.init()
        device = cuda.Device(0)
        self.ctx = device.make_context()

    def create(self, model):
        self.model = model
        TRT_LOGGER = trt.Logger(trt.Logger.INFO)

        with open(self.model, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
            self.engine = runtime.deserialize_cuda_engine(f.read())

        self.context = self.engine.create_execution_context()
        self.input_size = self.context.get_tensor_shape(self.engine.get_tensor_name(0))

        self.output_size = self.context.get_tensor_shape(self.engine.get_tensor_name(1))
        self.output = cuda.pagelocked_empty(tuple(self.context.get_tensor_shape(self.engine.get_tensor_name(1))),
                                            dtype=np.float32)

        self.d_input = cuda.mem_alloc(trt.volume(self.input_size) * trt.int32.itemsize)
        self.d_output = cuda.mem_alloc(self.output.nbytes)

        self.stream = cuda.Stream()
        self.bindings = [int(self.d_input), int(self.d_output)]

        for i in range(self.engine.num_io_tensors):
            self.context.set_tensor_address(self.engine.get_tensor_name(i), self.bindings[i])
        return self

    def __call__(self, input: np.uint8):
        input = (np.random.rand(580, 780, 3) * 255).astype(np.uint8)
        t1 = time.time()
        input = np.ascontiguousarray(np.float32(input / 255).transpose(2, 0, 1))
        input = input.reshape(1, *input.shape)
        cuda.memcpy_htod_async(self.d_input, input, self.stream)
        self.context.execute_async_v3(stream_handle=self.stream.handle)
        self.stream.synchronize()
        cuda.memcpy_dtoh_async(self.output, self.d_output, self.stream)
        self.stream.synchronize()
        result = np.clip(self.output[0].transpose(1, 2, 0), 0, 255).astype(np.uint8)
        print(f' FPS: {1/(time.time() - t1):.2f}')
        return np.ascontiguousarray(result)

    def clear(self):
        del self.context
        del self.engine
        del self.stream
        self.ctx.pop()
        self.ctx.detach()


if __name__ == '__main__':
    model = r'C:\Projects\DOE\src\pretrained_models\NAFNet.trt'

    inference = Inference()
    inference.create(model)

    input = (np.random.rand(580, 780, 3) * 255).astype(np.uint8)

    inference(input)
