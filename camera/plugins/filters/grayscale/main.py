from cv2 import cvtColor, COLOR_BGR2GRAY

import camera.webcam as webcam

SHAKE_INTENSITY = 2


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("greyscale", self.__newFrame, 4)

    def unload(self):
        webcam.removeNewFrameCallback("greyscale")

    def __newFrame(self, frame):
        return cvtColor(frame, COLOR_BGR2GRAY)
