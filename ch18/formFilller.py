import pyautogui, time

INTERVAL = 1

def autoFill():
    try:
        pyautogui.click(536, 422)
        pyautogui.typewrite('pyk')
        pyautogui.press('tab')
        pyautogui.typewrite('blood')
        pyautogui.press('tab')
        for i in range(4): pyautogui.press('down')
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.typewrite('no comments')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(INTERVAL)
        pyautogui.click(691, 299)
        time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print('stop by user')
    
    
for i in range(3):
    autoFill()
    