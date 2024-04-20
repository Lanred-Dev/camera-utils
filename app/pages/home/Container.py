from sys import modules

from PySide6.QtWidgets import QFrame, QHBoxLayout

import app.pages.home.plugins.Container as PluginContainer


class Container(QFrame):
    def __init__(self, root=None):
        super().__init__(root)

        self.setObjectName("homeContainer")
        self.setStyleSheet("#homeContainer { border-radius: 10px; padding: 15px; }")

        layout = QHBoxLayout(self)
        self.setLayout(layout)

        self.pluginContainer = PluginContainer(self)
        self.pluginContainer.setGeometry(0, 0, 500, self.height())
        layout.addWidget(self.pluginContainer)


modules[__name__] = Container
