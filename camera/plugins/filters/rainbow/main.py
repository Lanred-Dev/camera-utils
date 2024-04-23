from cv2 import applyColorMap, COLORMAP_JET

import camera.webcam as webcam

class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("rainbow", self.__newFrame, webcam.FILTER_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("rainbow")

    def __newFrame(self, frame):
        return applyColorMap(frame, COLORMAP_JET)
