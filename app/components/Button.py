from sys import modules

from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text=""):
        super().__init__(text)

        self.setStyleSheet(
            "background-color: #ff4747; border-radius: 10px; padding: 8px; color: #ffffff; font-size: 12px; font-weight: medium; margin: 0px;"
        )


modules[__name__] = Button
