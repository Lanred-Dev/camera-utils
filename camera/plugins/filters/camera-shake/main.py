from cv2 import warpAffine
from numpy import random, float32

import camera.webcam as webcam

SHAKE_INTENSITY = 2


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("camera-shake", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("camera-shake")

    def __newFrame(self, frame):
        rows, cols, _ = frame.shape

        dx = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        dy = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        M = float32([[1, 0, dx], [0, 1, dy]])

        return warpAffine(frame, M, (cols, rows))
