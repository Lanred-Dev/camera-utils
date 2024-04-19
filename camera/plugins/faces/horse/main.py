from cv2 import imread

import camera.webcam as webcam
import camera.detector as detector
import camera.overlay as overlay

baseOverlay = imread("camera\\plugins\\faces\\horse\\overlay.png", -1)


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("faces-horse", self.__newFrame, 0)

    def unload(self):
        webcam.removeNewFrameCallback("faces-horse")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)
        return overlay.overlayOnDetections(frame, baseOverlay, faces)
