import win32api
from time import sleep,time
def left_click_state():#If the left mouse button has been pressed return True 返回左键是否按下
    left_click = win32api.GetKeyState(0x01)
    return left_click < 0
def right_click_state():
    right_click = win32api.GetKeyState(0x02)
    return right_click < 0
def end_click_state():
    end_click = win32api.GetKeyState(0x23)
    return end_click < 0
def Dou2():#shake 抖动
    time1=0.015
    time2=0.025
    win32api.mouse_event(0x0001, -2, 3)
    sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, 2, -3)
        sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, -2, 3)
        sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, 2, -3)
        sleep(time2)
def Dou1():
    time1=0.015
    time2=0.025
    win32api.mouse_event(0x0001, -2, 2)
    sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, -1, 2)
        sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, 2, -2)
        sleep(time2)
    if left_click_state() and not right_click_state():
        win32api.mouse_event(0x0001, 1, -2)
        sleep(time2)
def main():
    k=0
    while True:
        if end_click_state():
            return
        sleep(0.001)
        if right_click_state():
                 temp = 0
                 # if left_click_state() and not right_click_state(): #此代码可以压前几枪
                 #    while(k<4):
                 #        sleep(0.05)
                 #        win32api.mouse_event(0x0001, 0, -15)
                 #        k+=1
                 while True:
                    sleep(0.001)
                    start = time()
                    if left_click_state() and not right_click_state():
                        Dou2()
                    sleep(0.001)
                    if left_click_state() and not right_click_state():
                        Dou1()
                    end = time()
                    temp+=end-start
                    sleep(0.001)
                    if temp >2.5 :
                        break
                    if end_click_state():
                        return
if __name__ == '__main__':
    main()
