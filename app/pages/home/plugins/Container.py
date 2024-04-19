from sys import modules
from functools import partial

from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QScrollArea,
)
from PySide6.QtCore import Qt

import camera.pluginController as pluginController
import app.components.ScrollContainer as ScrollContainer
import app.components.Title as Title
import app.pages.home.plugins.Plugin as Plugin


class Container(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__listItems = []

        self.setMinimumWidth(300)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        titleLabel = Title("Plugins", self)
        titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(titleLabel)

        self.scollContainer = ScrollContainer(self)
        layout.addWidget(self.scollContainer)

        self.__updateList()
        pluginController.addLoadCallback("appList", self.__updateList)
        pluginController.addUnloadCallback("appList", self.__updateList)

    def __updateList(self):
        for element in self.__listItems:
            element.deleteLater()

        self.__listItems = []

        for plugin in pluginController.plugins.values():
            container = Plugin(plugin)
            self.scollContainer.addWidget(container)
            self.__listItems.append(container)
            self.__listItems.append(container)


modules[__name__] = Container
