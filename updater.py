from sys import modules


class Updater:
    def __init__(self):
        self.updates = {}


modules[__name__] = Updater()
