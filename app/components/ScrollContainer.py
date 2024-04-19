from sys import modules

from PySide6.QtWidgets import QVBoxLayout, QWidget, QScrollArea
from PySide6.QtCore import Qt


class ScrollContainer(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(300)
        self.setWidgetResizable(True)
        self.setStyleSheet("QScrollArea { background: transparent; border: 0; }")
        self.viewport().setAutoFillBackground(False)
        self.viewport().setAttribute(Qt.WA_TranslucentBackground)

        contentContainer = QWidget()
        contentContainer.setObjectName("contentContainer")
        self.setStyleSheet("background: transparent; border: 0;")
        self.setWidget(contentContainer)

        self.contentContainerLayout = QVBoxLayout()
        contentContainer.setLayout(self.contentContainerLayout)

    def addWidget(self, widget: QWidget):
        return self.contentContainerLayout.addWidget(widget)


modules[__name__] = ScrollContainer
