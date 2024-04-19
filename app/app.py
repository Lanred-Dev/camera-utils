from sys import modules, argv, exit

from PySide6.QtWidgets import QApplication

import camera.controller as camera

import app.window as window


class App:
    def __init__(self):
        self.app = QApplication(argv)
        # self.app.aboutToQuit.connect(self.__close)

        self.window = window()
        self.window.show()

        self.app.exec()


modules[__name__] = App
