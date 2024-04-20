from sys import modules, argv, exit

from PySide6.QtWidgets import QApplication

import app.Window as Window


class App:
    def __init__(self):
        self.app = QApplication(argv)
        # self.app.aboutToQuit.connect(self.__close)

        self.window = Window()
        self.window.show()

        self.app.exec()


modules[__name__] = App
