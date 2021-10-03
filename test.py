import cv2 as cv
from Window_capture import WindowCapture
from vision import Vision


while(True):
    # 658, 34, 562, 1001

    Vision(WindowCapture(658, 34, 562, 1001), "D:\\cr.ss\\enemy\\enemy7.png")

    if cv.waitKey(1) == ord("q"):
        break

import cv2 as cv
import numpy as np
