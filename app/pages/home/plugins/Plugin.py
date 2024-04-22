from sys import modules

from PySide6.QtWidgets import QLabel, QPushButton

import camera.pluginController as pluginController
import app.components.Container as Container


class Plugin(Container):
    def __init__(self, plugin):
        super().__init__()

        self.name = plugin["name"]
        self.active = pluginController.isActive(self.name)
        
        nameLabel = QLabel(self.name + " [" + ("active" if self.active else "inactive") + "]")
        nameLabel.setStyleSheet(
            "font-size: 20px; color: #ffffff; font-weight: bold; margin: 0px;"
        )
        self.layout.addWidget(nameLabel)

        descriptionLabel = QLabel(plugin["description"])
        descriptionLabel.setStyleSheet("font-size: 14px; color: #C7C7C7; font-weight: bold; margin: 0px;")
        self.layout.addWidget(descriptionLabel)

        activateButton = QPushButton("Deactivate" if self.active else "Activate")
        activateButton.clicked.connect(self.__clicked)
        self.layout.addWidget(activateButton)

    def __clicked(self):
        if pluginController.isActive(self.name):
            pluginController.unload(self.name)
        else:
            pluginController.load(self.name)


modules[__name__] = Plugin
