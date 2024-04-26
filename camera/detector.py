from sys import modules

from cv2 import (
    resize,
    dnn,
)
from numpy import array, arange

EVERYTHING_CLASSES = [
    "background",
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tvmonitor",
]

faceNetwork = dnn.readNetFromCaffe(
    "camera\\models\\face\\model.prototxt.txt",
    "camera\\models\\face\\model.caffemodel",
)

everythingNetwork = dnn.readNetFromCaffe(
    "camera\\models\\everything\\model.prototxt.txt",
    "camera\\models\\everything\\model.caffemodel",
)


class Detector:
    def __init__(self):
        pass

    def detectFaces(self, frame):
        (h, w) = frame.shape[:2]

        blob = dnn.blobFromImage(
            resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)
        )

        faceNetwork.setInput(blob)
        detections = faceNetwork.forward()

        faces = []

        for index in range(0, detections.shape[2]):
            confidence = detections[0, 0, index, 2]

            if confidence < 0.5:
                continue

            box = detections[0, 0, index, 3:7] * array([w, h, w, h])

            faces.append(box.astype("int"))

        return faces

    def detectBottles(self, frame):
        detections = self.__detectEverything(frame)
        return [
            detection[1]
            for detection in filter(
                lambda detection: detection[0] == "bottle", detections
            )
        ]

    def __detectEverything(self, frame):
        detections = []

        (height, width) = frame.shape[:2]
        blob = dnn.blobFromImage(resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)

        everythingNetwork.setInput(blob)
        networkdetections = everythingNetwork.forward()

        for index in arange(0, networkdetections.shape[2]):
            confidence = networkdetections[0, 0, index, 2]

            if confidence < 0.5:
                continue

            box = networkdetections[0, 0, index, 3:7] * array(
                [width, height, width, height]
            )
            detections.append(
                [
                    EVERYTHING_CLASSES[int(networkdetections[0, 0, index, 1])],
                    box.astype("int"),
                ]
            )

        return detections


modules[__name__] = Detector()
