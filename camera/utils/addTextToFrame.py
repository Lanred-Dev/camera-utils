from sys import modules

from cv2 import putText, FONT_HERSHEY_SIMPLEX

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
    
modules[__name__] = addTextToFrame