import numpy as np
import warnings
warnings.simplefilter("ignore", DeprecationWarning)
import win32gui, win32ui, win32con
import cv2 as cv

def window_capture(x, y, w, h):

    hwnd = win32gui.FindWindow(None, "LDPlayer")
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (x, y), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)
    img = img[...,:3]
    img = np.ascontiguousarray(img)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img

cv.imshow("Game", window_capture(658, 34, 562, 1001))
if cv.waitKey(1) == ord("q"):
    cv.destroyAllWindows()
