from sys import modules

from PySide6.QtWidgets import QMainWindow

import app.pages.home.Container as HomeContainer


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera stuff")
        self.setFixedSize(600, 550)
        self.setStyleSheet("QMainWindow { background-color: #000000; }")

        self.setCentralWidget(HomeContainer())


modules[__name__] = Window
