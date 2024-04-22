from sys import modules

from PySide6.QtWidgets import QFrame, QHBoxLayout, QSpacerItem, QSizePolicy

import camera.webcam as webcam
import app.components.Label as Label
import app.components.Switch as Switch


class PreviewToggle(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.layout = QHBoxLayout(self)
            
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(3)
        self.setLayout(self.layout)

        label = Label("Show preview")
        label.setStyleSheet("font-size: 15px; font-weight: bold; color: #ffffff;")
        self.layout.addWidget(label)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addItem(spacer)

        switch = Switch()
        switch.on(self.__on)
        switch.off(self.__off)
        self.layout.addWidget(switch)

    def __on(self):
        webcam.showPreview = True

    def __off(self):
        webcam.showPreview = False


modules[__name__] = PreviewToggle
