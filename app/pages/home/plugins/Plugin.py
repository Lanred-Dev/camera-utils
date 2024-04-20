from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton

import camera.pluginController as pluginController


class Plugin(QFrame):
    def __init__(self, plugin):
        super().__init__()

        self.name = plugin["name"]
        self.active = pluginController.isActive(self.name)

        self.setStyleSheet(
            "background-color: #101112; border-radius: 10px; color: #ffffff; padding: 5px;"
        )

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


modules[__name__] = Plugin
