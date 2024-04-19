from sys import modules

import camera.webcam as webcam


class Controller:
    def __init__(self):
        self.active = False

    def __del__(self):
        global webcam
        del webcam

    def start(self):
        capturingWebcam = webcam.captureWebcam()
        self.active = capturingWebcam

        if capturingWebcam:
            webcam.setCameraFPS()
            webcam.startCapture()

        return capturingWebcam


modules[__name__] = Controller()
