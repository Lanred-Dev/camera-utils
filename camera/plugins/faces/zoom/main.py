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

        if faces:
            # Assume only one face is detected
            (x, y, w, h) = faces[0]

            # Calculate center of the face
            center_x = x + w // 2
            center_y = y + h // 2

            # Calculate the shift needed to center the face
            shift_x = frame.shape[1] // 2 - center_x
            shift_y = frame.shape[0] // 2 - center_y

            # Shift the face within the frame
            new_x = max(0, x + shift_x)
            new_y = max(0, y + shift_y)
            new_x_end = min(frame.shape[1], new_x + w)
            new_y_end = min(frame.shape[0], new_y + h)

            # Adjust the width if necessary to match the original width
            if new_x_end - new_x < w:
                new_x_end = new_x + w

            # Create a copy of the original frame
            new_frame = frame.copy()

            # Replace the face region in the original frame with the shifted face
            new_frame[y : y + h, x : x + w] = frame[new_y:new_y_end, new_x:new_x_end]
            frame = new_frame

        return frame
