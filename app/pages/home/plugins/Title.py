from sys import modules

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout

import camera.pluginController as pluginController
import app.components.Label as Label


class Title(QFrame):
    def __init__(self, group):
        super().__init__()

        self.setStyleSheet("margin-top: 25px; margin-bottom: 5px;")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        nameLabel = Label(group)
        nameLabel.setStyleSheet(
            nameLabel.styleSheet() + "font-size: 25px; color: #ffffff; font-weight: bold;"
        )
        layout.addWidget(nameLabel)

        pluginCountLabel = Label(
            str(len(pluginController.groups[group])) + " plugins in this group"
        )
        pluginCountLabel.setStyleSheet(
            pluginCountLabel.styleSheet() + "font-size: 15px; color: #C7C7C7; font-weight: bold;"
        )
        layout.addWidget(pluginCountLabel)


modules[__name__] = Title
