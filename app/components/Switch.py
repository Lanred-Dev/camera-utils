from sys import modules

from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Qt

import app.components.Button as Button


class Switch(QWidget):
    def __init__(self, wording=0):
        super().__init__()

        self.setProperty("checked", False)
        self.setStyleSheet(
            """QWidget[checked="true"] .on { background-color: #ff4747; } QWidget[checked="true"] .off { background-color: #212121; } QWidget[checked="false"] .off { background-color: #ff4747; } QWidget[checked="false"] .on { background-color: #212121; }"""
        )

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        onButton = Button("On" if wording == 1 else "Enable")
        onButton.setObjectName("on")
        onButton.setStyleSheet(
            onButton.styleSheet()
            + "border-top-right-radius: 0px; border-bottom-right-radius: 0px;"
        )
        self.on = onButton.clicked.connect
        self.on(self.__on)
        layout.addWidget(onButton)

        offButton = Button("Off" if wording == 1 else "Disable")
        offButton.setObjectName("off")
        offButton.setStyleSheet(
            offButton.styleSheet()
            + "border-top-left-radius: 0px; border-bottom-left-radius: 0px;"
        )
        self.off = offButton.clicked.connect
        self.off(self.__off)
        layout.addWidget(offButton)

    def __on(self):
        self.setProperty("checked", True)

    def __off(self):
        self.setProperty("checked", False)


modules[__name__] = Switch
