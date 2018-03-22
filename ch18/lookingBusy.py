import pyautogui, time

def lookingBusy():
    while 1:
        pyautogui.moveRel(1, 0)
        for i in range(10): time.sleep(1)
    
if __name__ == '__main__':
    lookingBusy()