import cv2 as cv
import numpy as np
from Window_capture import WindowCapture
from vision import Vision


wincap = WindowCapture("LDPlayer")

vision_ = Vision("D:\\cr.ss\\enemy\\enemy9.png")

while(True):
    screenshot = wincap.get_screenshot()
    screenshot = np.array(screenshot)

    points = vision_.find(screenshot, "rectangles")

    #cv.imshow("Screen", screenshot)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
