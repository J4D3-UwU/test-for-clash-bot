import cv2 as cv
import numpy as np
from Window_capture import window_capture
from vision import Vision


while(True):
    screenshot = window_capture(658, 34, 562, 1001)
    screenshot = np.array(screenshot)
    Vision(screenshot, "D:\\cr.ss\\enemy\\enemy7.png")


    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
