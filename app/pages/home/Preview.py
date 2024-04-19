from sys import modules

from PySide6.QtWidgets import QVBoxLayout, QFrame, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from cv2 import cvtColor, COLOR_BGR2RGB

import camera.webcam as webcam
import app.components.Title as Title


class Container(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(300)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        titleLabel = Title("Live preview", self)
        titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(titleLabel)

        self.image = QLabel(self)
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setFixedWidth(300)
        self.image.setStyleSheet("border-radius: 10px;")
        layout.addWidget(self.image)

        webcam.addNewFrameCallback("appPreview", self.__update, 999999999999)

    def __update(self, frame):
        correctedFrame = cvtColor(frame, COLOR_BGR2RGB)

        height, width, channels = correctedFrame.shape
        self.image.setPixmap(
            QPixmap.fromImage(
                QImage(
                    correctedFrame.data,
                    width,
                    height,
                    channels * width,
                    QImage.Format_RGB888,
                )
            )
        )

        return frame


modules[__name__] = Container
