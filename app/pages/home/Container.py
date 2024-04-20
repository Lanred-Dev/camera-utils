from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout

import app.pages.home.PreviewToggle as PreviewToggle
import app.pages.home.plugins.Container as PluginContainer


class Container(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("homeContainer")
        self.setStyleSheet("#homeContainer { border-radius: 10px; padding: 15px; }")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        previewToggle = PreviewToggle(self)
        previewToggle.setFixedWidth(500)
        layout.addWidget(previewToggle)

        pluginContainer = PluginContainer(self)
        pluginContainer.setGeometry(0, 0, 500, self.height())
        layout.addWidget(pluginContainer)


modules[__name__] = Container
