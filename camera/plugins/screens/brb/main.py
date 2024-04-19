from cv2 import putText, getTextSize, FONT_HERSHEY_SIMPLEX
from numpy import any

import camera.webcam as webcam


class Plugin:
    def __init__(self):
        self.__firstFrame = None

    def load(self):
        webcam.addNewFrameCallback("brb", self.__newFrame, webcam.SCREEN_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("brb")

    def __newFrame(self, frame):
        if not any(self.__firstFrame):
            (textWidth, textHeight) = getTextSize(
                "Be right back", FONT_HERSHEY_SIMPLEX, 0.8, 2
            )[0]

            textX = (frame.shape[1] - textWidth) // 2
            textY = (frame.shape[0] + textHeight) // 2

            self.__firstFrame = putText(
                frame,
                "Be right back",
                (textX, textY),
                FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 155),
                2,
            )

        return self.__firstFrame
