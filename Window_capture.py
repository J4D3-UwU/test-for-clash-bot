import cv2 as cv
import numpy as np
import win32gui
import win32ui
import win32con
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception("Window not found: {}".format(window_name))

        self.w = 561
        self.h = 1003

        window_rect = win32gui.GetWindowRect(self.hwnd)

        self.offset_x = window_rect[0] + 658
        self.offset_y = window_rect[1] + 34

    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (658,34), win32con.SRCCOPY)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype="uint8")
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        #img = np.ascontiguousarray(img)
        return img


        def get_screen_position(self, pos):
            return (pos[0] + self.offset_x, pos[1] + self.offset_y)
