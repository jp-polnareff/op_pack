import ctypes
import random
import time

from op.op_regist import op


def findColor(x1, y1, x2, y2, color, sim):
    return op.FindColor(x1, y1, x2, y2, color, sim, 0, )


def find_window(wind_class, title):
    return op.FindWindow(wind_class, title)


def bindWindow(hwnd, display, mouse, keypad, mode):
    return op.BindWindow(hwnd, display, mouse, keypad, mode)


def unBindWindow():
    return op.UnBindWindow()


def ocr(x1, y1, x2, y2, color_format, sim):
    return op.Ocr(x1, y1, x2, y2, color_format, sim)


def clickCommon():
    moveToAndLeftClick(579, 620)


def moveCommon():
    op.MoveTo(579, 620)


def findStr(x1, y1, x2, y2, string, color_format, sim):
    intX, intY = -1, -1
    res = op.FindStr(x1, y1, x2, y2, string, color_format, sim, intX, intY)
    return res[0], res[1], res[2]


def findStrExist(x1, y1, x2, y2, string, color_format, sim):
    return findStr(x1, y1, x2, y2, string, color_format, sim)[0] != -1


def moveToLeftUpDown(x, y):
    op.MoveTo(x, y)
    op.LeftUp()
    time.sleep(random.uniform(1, 2))
    op.LeftDown()
    time.sleep(random.uniform(1, 2))


def moveToAndLeftClick(x, y):
    op.MoveTo(x, y)
    op.leftClick()
    time.sleep(random.uniform(1, 2))


def moveToAndLeftDoubleClick(x, y):
    op.MoveTo(x, y)
    op.LeftDoubleClick()
    time.sleep(random.uniform(1, 2))


def findStrAndLeftClick(x1, y1, x2, y2, string, color_format, sim):
    res = findStr(x1, y1, x2, y2, string, color_format, sim)
    if res[0] == 0:
        moveToAndLeftClick(res[1], res[2])
        return True
    return False


def findStrAndLeftUpDown(x1, y1, x2, y2, string, color_format, sim):
    res = findStr(x1, y1, x2, y2, string, color_format, sim)
    if res[0] == 0:
        moveToLeftUpDown(res[1], res[2])
        return True
    return False


def findStrAndLeftClick(x1, y1, x2, y2, string, color_format, sim):
    res = findStr(x1, y1, x2, y2, string, color_format, sim)
    if res[0] == 0:
        moveToAndLeftClick(res[1], res[2])
        return True
    return False
