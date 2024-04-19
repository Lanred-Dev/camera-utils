from sys import modules
from threading import Thread
from copy import copy

from cv2 import (
    VideoCapture,
    destroyAllWindows,
    CAP_PROP_FRAME_WIDTH,
    CAP_PROP_FRAME_HEIGHT,
)
from pyvirtualcam import Camera, PixelFormat


class Webcam:
    def __init__(self):
        self.camera = None
        self.capture = None
        self.frame = None
        self.finalFrame = None
        self.active = False
        self.__captureThread = None
        self.__newFrameCallbacks = {}
        
        self.FILTER_PRIORITY = 3
        self.FACE_PRIORITY = 1
        self.SCREEN_PRIORITY = 4
        self.OVERLAY_PRIORITY = 2

    def __del__(self):
        self.capture.release()
        self.stopCapture()
        destroyAllWindows()

    def captureWebcam(self, index=0):
        capture = VideoCapture(index)

        if not capture.isOpened():
            return False

        self.capture = capture

        return True

    def startCapture(self):
        self.active = True
        self.__captureThread = Thread(target=self.__startCapture)
        self.__captureThread.start()

    def stopCapture(self):
        self.active = False

        if self.__captureThread:
            self.__captureThread.join()
            self.__captureThread = None

    def addNewFrameCallback(self, name, callback, priority=1):
        self.__newFrameCallbacks[name] = [priority, callback]

    def removeNewFrameCallback(self, name):
        del self.__newFrameCallbacks[name]

    def setCameraFPS(self, fps=40.0):
        self.__deleteCamera()
        self.__createCamera(fps)

    def __createCamera(self, fps):
        width = int(self.capture.get(CAP_PROP_FRAME_WIDTH))
        height = int(self.capture.get(CAP_PROP_FRAME_HEIGHT))

        self.camera = Camera(width, height, fps, fmt=PixelFormat.RGB, backend="obs")

    def __deleteCamera(self):
        if self.camera:
            self.camera = None

    def __startCapture(self):
        while self.active:
            self.__read()

            self.camera.send(self.finalFrame)
            self.camera.sleep_until_next_frame()

    def __read(self):
        success, frame = self.capture.read()

        if not success:
            return

        self.frame = frame
        self.finalFrame = frame

        for callback in sorted(
            copy(self.__newFrameCallbacks).values(), key=lambda x: x[0]
        ):
            self.finalFrame = callback[1](self.finalFrame)


modules[__name__] = Webcam()
