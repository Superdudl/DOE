import sys
import time

sys.path.append(__file__)

from pypylon import pylon
from pypylon import _genicam
import cv2
import numpy as np


class VideoCapture:
    def __init__(self):
        di = pylon.DeviceInfo()
        di.SetModelName('acA780-75gc')
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(di))
            self.camera.Open()
            self.camera.UserSetSelector.Value = "UserSet1"
        except _genicam.RuntimeException as e:
            print("Камера не подключена\n")
            self.camera = None
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_RGB8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        self.frame = None

    def start(self):
        if self.camera is not None:
            self.camera.UserSetLoad.Execute()
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def stop(self):
        if self.camera is not None:
            self.camera.StopGrabbing()
            time.sleep(0.1)
            self.camera.UserSetSave.Execute()
            self.camera.Close()

    def get_frame(self):
        grabResult = self.camera.RetrieveResult(11000, pylon.TimeoutHandling_ThrowException)
        try:
            if grabResult.GrabSucceeded():
                # Access the image data
                image = self.converter.Convert(grabResult)
                self.frame = image.GetArray()
            grabResult.Release()
        except _genicam.RuntimeException as e:
            self.frame = np.zeros((self.camera.Height.Value, self.camera.Width.Value, 3), dtype=np.uint8)
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
