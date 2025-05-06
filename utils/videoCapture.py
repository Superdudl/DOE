import sys
sys.path.append(__file__)

from pypylon import pylon
from pypylon import _genicam
import cv2


class VideoCapture:
    def __init__(self):
        di = pylon.DeviceInfo()
        di.SetModelName('acA780-75gc')
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(di))
            self.camera.Open()
        except _genicam.RuntimeException as e:
            print("Камера не подключена\n")
            self.camera = None
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_RGB8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        self.frame = None

    def start(self):
        if self.camera is not None:
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def stop(self):
        if self.camera is not None:
            self.camera.StopGrabbing()
            self.camera.Close()

    def get_frame(self):
        grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            # Access the image data
            image = self.converter.Convert(grabResult)
            self.frame = image.GetArray()
        grabResult.Release()
        return self.frame


if __name__ == "__main__":
    cam = VideoCapture()
    cam.start()
    cv2.namedWindow('GigE')
    while True:
        img = cam.get_frame()
        if img is None:
            break
        cv2.imshow('GigE', img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    cam.stop()
