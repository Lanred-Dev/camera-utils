from cv2 import copyMakeBorder

import camera.webcam as webcam
import camera.detector as detector

ZOOM_FACTOR = 2.0


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("faces-zoom", self.__newFrame, webcam.FACE_PRIORITY)

    def unload(self):
        webcam.removeNewFrameCallback("faces-zoom")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)

        if faces:
            ## TODO
            return frame

        return frame
