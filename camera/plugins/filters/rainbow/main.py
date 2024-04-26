from cv2 import cvtColor, addWeighted, COLOR_HSV2BGR
from numpy import zeros_like, uint8

import camera.webcam as webcam


class Plugin:
    def __init__(self):
        self.__shift = 0

    def load(self):
        webcam.addNewFrameCallback("rainbow", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("rainbow")

    def __newFrame(self, frame):
        self.__shift = (self.__shift + 1) % frame.shape[1]

        return addWeighted(frame, 0.7, self.__generateGradient(frame), 0.3, 0)

    def __generateGradient(self, frame):
        gradient = zeros_like(frame, dtype=uint8)

        for xIndex in range(frame.shape[1]):
            hue = (xIndex + self.__shift) % 180
            gradient[:, xIndex] = cvtColor(uint8([[[hue, 255, 255]]]), COLOR_HSV2BGR)[
                0
            ][0]

        return gradient
