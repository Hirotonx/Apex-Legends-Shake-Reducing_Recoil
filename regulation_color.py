"'使用方法：此为校准颜色脚本，开始后按下end键位即可校准颜色，按下Esc退出'"
import time
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
    print(1)
    saveDC.BitBlt((0,0), (w, h), mfcDC, (1500, 980), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
def end_click_state():
    end_click = win32api.GetKeyState(0x23)
    return end_click < 0
def Esc_click_state():
    end_click = win32api.GetKeyState(0x1B)
    return end_click < 0
while True:
    time.sleep(0.001)
    if Esc_click_state():
        break
    if end_click_state():
        window_capture("Temp.bmp")
        im = Image.open('Temp.bmp')
        # im.save('Temp.bmp', quality=50)
        print('hvae:', im.getpixel((91, 30)))  # 有枪管稳定器武器校准
        print('lack:', im.getpixel((63, 30)))  # 无枪管稳定器校准
        time.sleep(1)
