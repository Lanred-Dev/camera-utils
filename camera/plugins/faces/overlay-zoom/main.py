from cv2 import resize

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

        for startX, startY, endX, endY in faces:
            face_roi = frame[startY:endY, startX:endX]

            zoomed_face = resize(face_roi, None, fx=ZOOM_FACTOR, fy=ZOOM_FACTOR)

            startX = max(
                startX - int((ZOOM_FACTOR - 1) * (endX - startX) / 2), 0
            )
            startY = max(
                startY - int((ZOOM_FACTOR - 1) * (endY - startY) / 2), 0
            )
            
            endX = min(startX + zoomed_face.shape[1], frame.shape[1])
            endY = min(startY + zoomed_face.shape[0], frame.shape[0])

            frame[startY:endY, startX:endX] = zoomed_face[:endY - startY, :endX - startX]

        return frame
