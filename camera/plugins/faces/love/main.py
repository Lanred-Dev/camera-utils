from cv2 import imread

import camera.webcam as webcam
import camera.detector as detector
import camera.overlay as overlay

baseOverlay = imread("camera\\plugins\\love\\overlay.png", -1)


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("love", self.__newFrame, 0)

    def unload(self):
        webcam.removeNewFrameCallback("love")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)
        return overlay.overlayOnDetections(frame, baseOverlay, faces)
