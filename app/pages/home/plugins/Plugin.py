from sys import modules

from PySide6.QtWidgets import QPushButton

import camera.pluginController as pluginController
import app.components.Container as Container
import app.components.Label as Label


class Plugin(Container):
    def __init__(self, plugin):
        super().__init__()

        self.name = plugin["name"]
        self.active = pluginController.isActive(self.name)
        
        nameLabel = Label(self.name + " [" + ("active" if self.active else "inactive") + "]")
        nameLabel.setStyleSheet(nameLabel.styleSheet() + "font-size: 20px; color: #ffffff; font-weight: bold;")
        self.layout.addWidget(nameLabel)

        descriptionLabel = Label(plugin["description"])
        descriptionLabel.setStyleSheet(descriptionLabel.styleSheet() + "font-size: 14px; color: #C7C7C7;")
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
