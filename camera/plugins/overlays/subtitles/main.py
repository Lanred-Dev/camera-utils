from time import sleep, ctime
from textwrap import wrap
from threading import Thread

from cv2 import putText, getTextSize, FONT_HERSHEY_SIMPLEX, LINE_AA
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

import camera.webcam as webcam

recognizer = Recognizer()
recognizer.pause_threshold = 0.05
recognizer.non_speaking_duration = 0.03
microphone = Microphone()

microphoneInputs = []
microphoneInput = ""
listeningForMicrophoneInput = False

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)


def updateMicrophoneInput():
    global microphoneInputs
    global microphoneInput

    microphoneInput = ""

    sortedMicrophoneInputs = sorted(microphoneInputs, key=lambda x: x["time"])

    for inputData in sortedMicrophoneInputs:
        microphoneInput += inputData["text"]


def listenForInput():
    global listeningForMicrophoneInput
    global microphoneInputs
    global microphoneInput

    if listeningForMicrophoneInput:
        return

    listeningForMicrophoneInput = True
    input = ""

    with microphone as source:
        audioData = recognizer.listen(source)

    try:
        input = recognizer.recognize_wit(
            audioData, key="5LTIXOXREJLD2NOQE66AR32X2HZSFBDM"
        )
    except UnknownValueError as error:
        input = ""
    except RequestError as error:
        input = ""

    if len(input) > 0:
        currentTime = ctime()
        microphoneInputs.append({"time": currentTime, "text": input})

        updateMicrophoneInput()

        listeningForMicrophoneInput = False

        sleep(0.2 * len(input))

        for inputData in microphoneInputs:
            if inputData["time"] != currentTime:
                continue

            microphoneInputs.remove(inputData)
            break

        updateMicrophoneInput()
    else:
        listeningForMicrophoneInput = False


def addTextToFrame(frame, text, position):
    return putText(
        frame,
        text,
        position,
        FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 155),
        2,
    )


class Plugin:
    def __init__(self):
        self.__active = False

    def load(self):
        self.__active = True

        webcam.addNewFrameCallback("subtitles", self.__newFrame, 1)

        while self.__active:
            Thread(target=listenForInput).start()

    def unload(self):
        self.__active = False

        webcam.removeNewFrameCallback("subtitles")

    def __newFrame(self, frame):
        if len(microphoneInput) == 0:
            return frame

        (_textWidth, textHeight), _baseline = getTextSize(
            microphoneInput, FONT_HERSHEY_SIMPLEX, 0.8, 2
        )
        wrappedText = wrap(microphoneInput, width=45)
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
