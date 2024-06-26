from cv2 import imread

import camera.webcam as webcam
import camera.detector as detector
import camera.overlay as overlay

baseOverlay = imread("camera\\plugins\\faces\\ginger\\overlay.png", -1)


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback(
            "faces-ginger", self.__newFrame, webcam.FACE_PRIORITY
        )

    def unload(self):
        webcam.removeNewFrameCallback("faces-ginger")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)
        return overlay.overlayOnDetections(frame, baseOverlay, faces)
