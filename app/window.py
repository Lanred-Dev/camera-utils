from sys import modules

from PySide6.QtWidgets import QMainWindow

import app.pages.home.Container as HomeContainer


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera utils")
        self.setFixedSize(525, 500)
        self.setStyleSheet("QMainWindow { background-color: #050505; }")

        self.setCentralWidget(HomeContainer())


modules[__name__] = Window
