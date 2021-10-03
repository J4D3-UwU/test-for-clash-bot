import cv2 as cv
import numpy as np

def Vision(haystack, needle):
    # "D:\\cr.ss\\screen_randon.png"
    screen = cv.imread(haystack, cv.IMREAD_UNCHANGED)
    # "D:\\cr.ss\\enemy\\enemy7.png"
    enemy_lvl = cv.imread(needle, cv.IMREAD_UNCHANGED)
    needle_w = enemy_lvl.shape[1]
    needle_h = enemy_lvl.shape[0]

    result = cv.matchTemplate(screen, enemy_lvl, cv.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    if len(rectangles) :
        line_color = (0, 255, 0)
        line_type = cv.LINE_4


        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(screen, top_left, bottom_right, line_color, line_type)
        cv.imshow("matches 7", screen)
        cv.waitKey()


    points = []
    if len(rectangles):

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:

            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h*2)
            # Save the points
            points.append((center_x, center_y))
    return points    
