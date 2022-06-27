import win32api
from time import sleep,time
from recognition import regulation_color
Shake=[[-2,2,-2,2,-2,2,-2,2],[0,-2,0,2,0,-2,0,2]]
Shake1=[[-2,2,-2,2,-2,2,-2,2],[0,-1,0,1,0,-1,0,1]]
open_regulation=True#激活识别瞄准镜
zero=0

def left_click_state():#If the left mouse button has been pressed return True 返回左键是否按下
    left_click = win32api.GetKeyState(0x01)
    return left_click < 0

def right_click_state():
    right_click = win32api.GetKeyState(0x02)
    return right_click < 0

def end_click_state():
    end_click = win32api.GetKeyState(0x23)
    return end_click < 0

def switch():
    if open_regulation:
        return regulation_color()
    else: 
        return True
    
def dou():
    while True:
        sleep(0.001)
        k=0
        if left_click_state() and not right_click_state(): #此代码可以压前几枪
            if switch():
             while(k<4):
                sleep(0.05)
                win32api.mouse_event(0x0001, 0, 5)
                k+=1
            if(k==4):
                break
def Dou2():#shake 抖动
    time1=0.015
    time2=0.025
    global zero
    global Shake
    for i in range(0,4):
        if left_click_state() and not right_click_state():
            if switch():
                win32api.mouse_event(0x0001, Shake1[0][i], Shake1[1][i])
                sleep(time2)
                if (i == 3):
                    win32api.mouse_event(0x0001, 0, 1)

def Dou1():
    time1=0.015
    time2=0.025
    global zero
    global Shake
    for i in range(4,8):
        if left_click_state() and not right_click_state():
            if switch():
                win32api.mouse_event(0x0001, Shake1[0][i], Shake1[1][i])
                sleep(time1)
                if (i == 7):
                    win32api.mouse_event(0x0001, 0, 1)
def main():
    global open_regulation
    while True:
        if end_click_state():
            return
        sleep(0.007)
        if right_click_state():
                 dou()
                 temp = 0
                 while True:
                    sleep(0.001)
                    start = time()
                    if right_click_state():
                        temp=0
                    Dou2()
                    if right_click_state():
                        temp=0
                    Dou1()
                    end = time()
                    if right_click_state():
                        temp=0
                    temp+=end-start
                    sleep(0.001)
                    if temp >3 :
                        break
                    if end_click_state():
                        return
                 print(1)
if __name__ == '__main__':
    main()
