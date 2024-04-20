from sys import modules

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy

import camera.webcam as webcam
import app.components.Switch as Switch


class PreviewToggle(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        label = QLabel("Show preview", self)
        label.setStyleSheet("font-size: 15px; font-weight: bold;")
        layout.addWidget(label)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)

        switch = Switch(self)
        switch.on(self.__on)
        switch.off(self.__off)
        layout.addWidget(switch)

    def __on(self):
        webcam.showPreview = True

    def __off(self):
        webcam.showPreview = False


modules[__name__] = PreviewToggle
