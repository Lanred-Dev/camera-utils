from cv2 import addWeighted
from numpy import zeros_like, uint8

import camera.webcam as webcam


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("rainbow", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("rainbow")

    def __newFrame(self, frame):
        rainbowGradient = zeros_like(frame, dtype=uint8)

        for index in range(frame.shape[1]):
            rainbowGradient[:, index] = [
                255 * index // frame.shape[1],
                0,
                255 - (255 * index // frame.shape[1]),
            ]

        return addWeighted(frame, 0.7, rainbowGradient, 0.3, 0)
