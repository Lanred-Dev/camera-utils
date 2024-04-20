from sys import modules, argv, exit

from PySide6.QtWidgets import QApplication

import camera.controller as camera
import app.Window as Window


class App:
    def __init__(self):
        self.app = QApplication(argv)
        self.app.aboutToQuit.connect(self.__close)

        self.window = Window()
        self.window.show()

        self.app.exec()

    def __close(self):
        camera.stop()

        exit()


modules[__name__] = App
