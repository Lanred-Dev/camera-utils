from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

import camera.pluginController as pluginController
import app.components.ScrollContainer as ScrollContainer
import app.pages.home.plugins.Title as Title
import app.pages.home.plugins.Plugin as Plugin


class Container(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__listItems = []

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.scollContainer = ScrollContainer(self)
        self.scollContainer.setFixedWidth(500)
        self.scollContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.scollContainer)

        self.__updateList()
        pluginController.addLoadCallback("appList", self.__updateList)
        pluginController.addUnloadCallback("appList", self.__updateList)

    def __updateList(self):
        for element in self.__listItems:
            element.deleteLater()

        self.__listItems = []

        for group, plugins in pluginController.groups.items():
            title = Title(group)
            self.scollContainer.addWidget(title)
            self.__listItems.append(title)

            for plugin in pluginController.plugins.values():
                if not plugin["name"] in plugins:
                    continue

                container = Plugin(plugin)
                self.scollContainer.addWidget(container)
                self.__listItems.append(container)


modules[__name__] = Container
