from cv2 import rectangle

import camera.webcam as webcam
import camera.detector as detector


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("faces-cover", self.__newFrame, 0)

    def unload(self):
        webcam.removeNewFrameCallback("faces-cover")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)

        for startX, startY, endX, endY in faces:
            rectangle(frame, (startX, startY), (endX, endY), (0, 0, 0), -1)

        return frame
