from time import sleep, ctime
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
        self.__text = None
        self.__recognizedTexts = []
        self.__recognizerModel = None
        self.__recognizer = None
        self.__portAudio = None
        self.__audioStream = None

    def load(self):
        self.__active = True
        
        self.__recognizerModel = Model(lang="en-us")
        self.__recognizer = KaldiRecognizer(self.__recognizerModel, 16000)

        self.__portAudio = PyAudio()
        self.__audioStream = self.__portAudio.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

        webcam.addNewFrameCallback("subtitles", self.__newFrame, webcam.OVERLAY_PRIORITY)

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
                
                for word, index in result["text"].split(" "):
                    self.__newWord(word, index)
                    
                self.__formatRecognizedText()
                
    def __newWord(self, word, index):
        time = ctime()
        self.__recognizedTexts.append({ "text": word, "time": time, "id": index })
        
        sleep(0.3)
        
        for data in self.__recognizedTexts:
            if data["time"] != time and data["id"] != index:
                continue

            self.__recognizedTexts.remove(data)
            break
                
    def __formatRecognizedText(self):
        sortedTexts = sorted(self.__recognizedTexts, key=lambda x: x["time"])

        for data in sortedTexts:
            self.__text += data["text"]