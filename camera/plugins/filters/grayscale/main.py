from cv2 import cvtColor, merge, COLOR_BGR2GRAY

import camera.webcam as webcam


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("grayscale", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("grayscale")

    def __newFrame(self, frame):
        grayFrame = cvtColor(frame, COLOR_BGR2GRAY)
        return merge([grayFrame, grayFrame, grayFrame])
