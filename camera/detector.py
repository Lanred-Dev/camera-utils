from sys import modules

from cv2 import (
    resize,
    dnn,
)
from numpy import array

network = dnn.readNetFromCaffe(
    "camera\\models\\face.prototxt.txt",
    "camera\\models\\face.caffemodel",
)


class Detector:
    def __init__(self):
        pass

    def detectFaces(self, frame):
        (h, w) = frame.shape[:2]

        blob = dnn.blobFromImage(
            resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)
        )

        network.setInput(blob)
        detections = network.forward()

        faces = []

        for index in range(0, detections.shape[2]):
            confidence = detections[0, 0, index, 2]

            if confidence < 0.5:
                continue

            box = detections[0, 0, index, 3:7] * array([w, h, w, h])

            faces.append(box.astype("int"))

        return faces


modules[__name__] = Detector()
