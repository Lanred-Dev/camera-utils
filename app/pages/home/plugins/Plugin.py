from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton

import camera.pluginController as pluginController


class PluginContainer(QFrame):
    def __init__(self, plugin):
        super().__init__()

        self.name = plugin["name"]
        self.active = pluginController.isActive(self.name)

        self.setStyleSheet("background-color: lightgray; border-radius: 10px;")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        nameLabel = QLabel(
            self.name + " [" + ("active" if self.active else "inactive") + "]"
        )
        layout.addWidget(nameLabel)

        descriptionLabel = QLabel(plugin["description"])
        layout.addWidget(descriptionLabel)

        activateButton = QPushButton("Deactivate" if self.active else "Activate")
        activateButton.clicked.connect(self.__clicked)
        layout.addWidget(activateButton)

    def __clicked(self):
        if pluginController.isActive(self.name):
            pluginController.unload(self.name)
        else:
            pluginController.load(self.name)


modules[__name__] = PluginContainer
