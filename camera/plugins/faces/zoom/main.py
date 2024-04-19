from cv2 import resize

import camera.webcam as webcam
import camera.detector as detector

ZOOM_FACTOR = 2.0


class Plugin:
    def __init__(self):
        pass

    def load(self):
        webcam.addNewFrameCallback("faces-zoom", self.__newFrame, 0)

    def unload(self):
        webcam.removeNewFrameCallback("faces-zoom")

    def __newFrame(self, frame):
        faces = detector.detectFaces(frame)

        if faces:
            (start_x, start_y, end_x, end_y) = faces[0]

            face_roi = frame[start_y:end_y, start_x:end_x]

            zoomed_face = resize(face_roi, None, fx=ZOOM_FACTOR, fy=ZOOM_FACTOR)

            new_start_x = max(
                start_x - int((ZOOM_FACTOR - 1) * (end_x - start_x) / 2), 0
            )
            new_start_y = max(
                start_y - int((ZOOM_FACTOR - 1) * (end_y - start_y) / 2), 0
            )
            new_end_x = min(new_start_x + zoomed_face.shape[1], frame.shape[1])
            new_end_y = min(new_start_y + zoomed_face.shape[0], frame.shape[0])

            frame[new_start_y:new_end_y, new_start_x:new_end_x] = zoomed_face[
                : new_end_y - new_start_y, : new_end_x - new_start_x
            ]

        return frame
