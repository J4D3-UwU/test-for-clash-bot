from Window_capture import WindowCapture
from vision import Vision
from time import time

loop_time = time()
wincap = WindowCapture("LDPlayer")

vision_ = Vision("D:\\cr.ss\\enemy\\enemy5.png")
vision_6 = Vision("D:\\cr.ss\\enemy\\enemy6.png")
vision_7 = Vision("D:\\cr.ss\\enemy\\enemy7.png")
vision_8 = Vision("D:\\cr.ss\\enemy\\enemy8.png")
vision_9 = Vision("D:\\cr.ss\\enemy\\enemy9.png")

while(True):
    screenshot = np.array(wincap.get_screenshot(695, 108, 481, 662))
    points = vision_.find(screenshot, "computer_vision", "rectangles") + vision_6.find(screenshot, "computer_vision", "rectangles") + vision_7.find(screenshot, "computer_vision", "rectangles") + vision_8.find(screenshot, "computer_vision", "rectangles") + vision_9.find(screenshot, "computer_vision", "rectangles")

    print("FPS {}".format(1 / (time() - loop_time)))
    loop_time = time()

    #cv.imshow("Screen", screenshot)
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
