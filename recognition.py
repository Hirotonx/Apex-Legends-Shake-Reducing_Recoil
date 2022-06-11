import win32gui, win32ui, win32con, win32api
from PIL import Image
def window_capture(filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = 180
    h = 50
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (w, h), mfcDC, (1500, 980), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
def regulation_color():
    window_capture("Temp.bmp")
    im = Image.open('Temp.bmp')
    have=im.getpixel((91, 30))
    lack=im.getpixel((63, 30))
    #如果有滤镜或者更改了图片更改下面的验证方式
    if(have[1]-have[0]>0 and have[2]-have[0]>20):
        have='blue'
    elif (have[1] - have[0] < 0 and have[2] - have[0] > 20):
        have = 'purple'
    else:
        have='0'
    if (lack[1] - lack[0] < 0 and lack[2] - lack[0] > 20):
        lack = 'purple'
    elif (lack[1] - lack[0] > 0 and lack[2] - lack[0] > 20):
        lack = 'purple'
    else:
        lack='0'
    if ((have=='blue' or have=='purple')or(lack=='blue' or lack=='purple')):
        return True
    else:
        return False
