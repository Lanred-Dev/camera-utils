from sys import modules

from PySide6.QtWidgets import QFrame, QVBoxLayout

class Container(QFrame):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet(
            "background-color: #101112; border-radius: 10px; color: #ffffff; padding: 15px 30px;"
        )

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(3)
        self.setLayout(self.layout)


modules[__name__] = Container
