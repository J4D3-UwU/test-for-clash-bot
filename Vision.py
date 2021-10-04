import cv2 as cv
import numpy as np

class Vision():

    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]
        self.method = method



    def find(self, haystack_img, name, debug_mode=None):

        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        threshold = 0.783
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        #print(locations)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.3)
        #print(rectangles)

        points = []
        if len(rectangles):

            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (0, 255, 0)
            marker_type = cv.MARKER_CROSS

            for (x, y, w, h) in rectangles:

                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                points.append((center_x, center_y))

                if debug_mode == "rectangles":
                    top_left = (x, y)
                    bottom_tight = (x + w, y + h)
                    cv.rectangle(haystack_img, top_left, bottom_tight, line_color, line_type)
                elif debug_mode == "points":
                    cv.drawMarker(haystack_img, (center_x, center_y), marker_color, marker_type)
        if debug_mode:
            cv.imshow(name, haystack_img)
        return points

