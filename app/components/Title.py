from sys import modules

from PySide6.QtWidgets import QLabel


class Title(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName("title")
        self.setStyleSheet(
            "#title { font-size: 25px; margin-top: 5px; margin-bottom: 5px; font-weight: bold; color: #ffffff; }"
        )


modules[__name__] = Title
