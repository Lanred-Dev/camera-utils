from time import time
from textwrap import wrap

from cv2 import getTextSize, FONT_HERSHEY_SIMPLEX
from vosk import KaldiRecognizer, Model
from pyaudio import PyAudio, paInt16
from json import loads

import camera.webcam as webcam
import camera.utils.addTextToFrame as addTextToFrame


class Plugin:
    def __init__(self):
        self.__active = False
        self.__text = ""
        self.__recognizedTexts = []
        self.__recognizer = None
        self.__portAudio = None
        self.__audioStream = None

    def load(self):
        self.__active = True

        recognizerModel = Model(model_path="camera\\models\\speech\\english")
        self.__recognizer = KaldiRecognizer(recognizerModel, 16000)

        self.__portAudio = PyAudio()
        self.__audioStream = self.__portAudio.open(
            format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192
        )

        webcam.addNewFrameCallback(
            "subtitles", self.__newFrame, webcam.OVERLAY_PRIORITY
        )

        self.__startSpeechRecognizer()

    def unload(self):
        self.__active = False

        self.__audioStream.stop_stream()
        self.__audioStream.close()
        self.__portAudio.terminate()

        webcam.removeNewFrameCallback("subtitles")

    def __newFrame(self, frame):
        if len(self.__text) == 0:
            return frame

        currentTime = time()

        for data in self.__recognizedTexts:
            print(currentTime, data["endTime"])
            if currentTime < data["endTime"]:
                continue

            self.__recognizedTexts.remove(data)
            break

        (_textWidth, textHeight), _baseline = getTextSize(
            self.__text, FONT_HERSHEY_SIMPLEX, 0.8, 2
        )
        wrappedText = wrap(self.__text, width=45)
        totalTextHeight = textHeight * len(wrappedText)
        startYPosition = (frame.shape[0] - 15) - totalTextHeight
        currentYPosition = startYPosition

        for line in wrappedText:
            (textWidth, _textHeight), _baseline = getTextSize(
                line, FONT_HERSHEY_SIMPLEX, 0.8, 2
            )

            frame = addTextToFrame(
                frame,
                line,
                ((frame.shape[1] // 2) - (textWidth // 2), currentYPosition),
            )

            currentYPosition += textHeight + 2

        return frame

    def __startSpeechRecognizer(self):
        while self.__active:
            data = self.__audioStream.read(4096)

            if self.__recognizer.AcceptWaveform(data):
                result = loads(self.__recognizer.Result())

                for index, word in enumerate(result["text"].split(" ")):
                    self.__newWord(word, index)

            self.__formatRecognizedText()

    def __newWord(self, word, index):
        if len(word) <= 0:
            return

        currentTime = time()
        print(str((currentTime + (0.3 * (index + 1)) - currentTime)))
        self.__recognizedTexts.append(
            {
                "text": word,
                "time": currentTime,
                "endTime": currentTime + (0.3 * (index + 1)),
            }
        )

    def __formatRecognizedText(self):
        self.__text = ""

        for data in sorted(self.__recognizedTexts, key=lambda x: x["time"]):
            self.__text += " " + data["text"]
