"'https://github.com/Hirotonx/Apex-Legends-Shake-Reducing_Recoil'"
import win32api
from time import sleep,time
Shake0=[[-2,2,-2,2,-2,-1,2,1],[3,-3,3,-3,2,2,-2,-2]]
Shake1=[[-1,1,-1,1,-1,-1,1,1],[1,-1,1,-1,1,-1,1,-1]]
#If the left mouse button has been pressed return True 返回左键是否按下
def left_click_state():
    left_click = win32api.GetKeyState(0x01)
    return left_click < 0
def right_click_state():
    right_click = win32api.GetKeyState(0x02)
    return right_click < 0
def end_click_state():
    end_click = win32api.GetKeyState(0x23)
    return end_click < 0
def dou():
    k=0
    if left_click_state() and not right_click_state(): #此代码可以压前几枪
     while(k<4):
        sleep(0.045)
        win32api.mouse_event(0x0001, 0, 15)
        k+=1
def Dou2():#shake 抖动
    time1=0.015
    time2=0.025
    global Shake
    for i in range(0,4):
        if left_click_state() and not right_click_state():
            win32api.mouse_event(0x0001, Shake1[0][i], Shake1[1][i])
            sleep(time1)
def Dou1():
    time1=0.015
    time2=0.025
    global Shake
    for i in range(4,8):
        if left_click_state() and not right_click_state():
            win32api.mouse_event(0x0001, Shake1[0][i], Shake1[1][i])
            sleep(time1)
def main():
    while True:
        if end_click_state():
            return
        sleep(0.001)
        if right_click_state():
                 dou()
                 temp = 0
                 while True:
                    sleep(0.001)
                    start = time()
                    Dou2()
                    if right_click_state():
                        temp=0
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
