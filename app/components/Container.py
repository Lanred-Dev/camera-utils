from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout


class Container(QFrame):
    def __init__(self, parent=None, layout="v"):
        super().__init__(parent)

        self.setStyleSheet(
            "background-color: #101112; border-radius: 10px; color: #ffffff; padding: 22px;"
        )

        if layout == "v":
            self.layout = QVBoxLayout(self)
        else:
            self.layout = QHBoxLayout(self)

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)


modules[__name__] = Container
