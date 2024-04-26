from cv2 import imread

import camera.webcam as webcam
import camera.detector as detector
import camera.overlay as overlay

baseOverlay = imread("camera\\plugins\\bottle-replacers\\chicken\\overlay.png", -1)


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback(
            "bottle-replacers-chicken", self.__newFrame, webcam.FACE_PRIORITY
        )

    def unload(self):
        webcam.removeNewFrameCallback("bottle-replacers-chicken")

    def __newFrame(self, frame):
        bottles = detector.detectBottles(frame)
        return overlay.overlayOnDetections(frame, baseOverlay, bottles)
