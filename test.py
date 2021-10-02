import cv2 as cv
from time import time
from Window_capture import window_capture


loop_time = time()
while(True):

    my_back_left = window_capture(704, 664, 235, 108)
    my_back_right = window_capture(940, 664, 235, 108)
    my_front_left = window_capture(704, 525, 235, 125)
    my_front_right = window_capture(940, 525, 235, 125)
    middle_left = window_capture(704, 370, 235, 155)
    middle_right = window_capture(940, 370, 235, 155)
    enemy_left = window_capture(704, 208, 235, 162)
    enemy_right = window_capture(940, 208, 235, 162)

    cv.imshow("4L", my_back_left)
    cv.imshow("4R", my_back_right)
    cv.imshow("3L", my_front_left)
    cv.imshow("3R", my_front_right)
    cv.imshow("2L", middle_left)
    cv.imshow("2R", middle_right)
    cv.imshow("1L", enemy_left)
    cv.imshow("1R", enemy_right)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord("q"):
        break
