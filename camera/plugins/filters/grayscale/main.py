from cv2 import cvtColor, COLOR_BGR2GRAY

import camera.webcam as webcam

SHAKE_INTENSITY = 2


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("grayscale", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("grayscale")

    def __newFrame(self, frame):
        return cvtColor(frame, COLOR_BGR2GRAY)
