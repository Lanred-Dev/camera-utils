from sys import modules

from PySide6.QtWidgets import QLabel

class Label(QLabel):
    def __init__(self, text=""):
        super().__init__(text)
        
        self.setStyleSheet("padding: 0px; margin: 0px;")


modules[__name__] = Label
