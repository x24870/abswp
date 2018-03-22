#Fill the form automatically
#Form link: https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

import pyautogui, time

formData = [{'name': '趕羚羊', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 1, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of thebreak room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the publictrust. Uphold the law.'},
           ]

INTERVAL = 3

def autoFill(data):
    print('You have %d sec to stop this process.' % INTERVAL)
    for i in range(INTERVAL):
        print(INTERVAL-i)
        time.sleep(1)
    
    try:
        pyautogui.PAUSE = 0.5
        pyautogui.click(346, 338)
        pyautogui.typewrite(data['name'])
        pyautogui.press('tab')
        
        pyautogui.typewrite(data['fear'])
        pyautogui.press('tab')
        
        if data['source'] == 'wand':
            pyautogui.typewrite(['down', '\t'])
        elif data['source'] == 'amulet':
            pyautogui.typewrite(['down', 'down', '\t'])
        elif data['source'] == 'crystal ball':
            pyautogui.typewrite(['down', 'down', 'down', '\t'])
        elif data['source'] == 'money':
            pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])
            
        if data['robocop'] == 1:
            pyautogui.typewrite([' ', '\t'])
        elif data['robocop'] == 2:
            pyautogui.typewrite(['right', 'right', '\t'])
        elif data['robocop'] == 3:
            pyautogui.typewrite(['right', 'right', 'right', '\t'])
        elif data['robocop'] == 4:
            pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])
        elif data['robocop'] == 5:
            pyautogui.typewrite(['right', 'right', 'right', 'right', 'right', '\t'])
        
        pyautogui.typewrite(data['comments'])
        pyautogui.press('tab')
        
        pyautogui.press('enter')
        
        time.sleep(1)
        pyautogui.click(463, 239)
        time.sleep(1)
    except KeyboardInterrupt:
        print('stop by user')
    
    
for data in formData:
    autoFill(data)
    