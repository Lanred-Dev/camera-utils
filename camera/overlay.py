from sys import modules

from cv2 import (
    merge,
    resize,
    bitwise_not,
    bitwise_and,
    add,
)

EXTRA_PIXELS = 50


class Overlay:
    def __init__(self):
        pass

    def overlayOnDetections(self, frame, baseOverlay, detections):
        if len(detections) == 0:
            return frame

        for startX, startY, endX, endY in detections:
            width = (endX - startX) + EXTRA_PIXELS
            height = (endY - startY) + EXTRA_PIXELS
            startX = startX - (EXTRA_PIXELS // 2)
            startY = startY - (EXTRA_PIXELS // 2)

            if startX < 0 or startY < 0:
                continue

            sizedOverlay = resize(baseOverlay, (width, height))

            regionOfInterest = frame[startY : startY + height, startX : startX + width]

            alphaChannel = sizedOverlay[:, :, 3]

            mask = merge((alphaChannel, alphaChannel, alphaChannel))

            overlay = sizedOverlay[:, :, :3]

            regionOfInterest = bitwise_and(regionOfInterest, bitwise_not(mask))

            overlay = bitwise_and(overlay, mask)

            regionOfInterest = add(regionOfInterest, overlay)

            frame[startY : startY + height, startX : startX + width] = regionOfInterest

        return frame


modules[__name__] = Overlay()
