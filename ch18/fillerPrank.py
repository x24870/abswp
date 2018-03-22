#My friend ask me to fill this form, she says she needs more result.
#So I decide to help her. You are welcome!

import pyautogui, random, time

pyautogui.PAUSE = 0.1

SPEAKER = ['Tom Cruise', 'Bradley Pitt', 'Jennifer Lawrence', 'Donny Yen', 'Bruce Lee'
           'Peter Jackson', 'Elon Musjk', 'LeBron James', 'May J Lee', 'Emily Blunt']

def generateData():
    data = {}
    
    #Q1*
    data.setdefault('spendTime', random.randint(1, 7))
    #Q2*
    adPrefer = ['1','2','3','4','5']
    random.shuffle(adPrefer)
    data.setdefault('adPrefer', adPrefer)
    #Q3* if know == 2, skip to basic info
    data.setdefault('know', random.randint(1, 2))
    #increase the chance of know this game
    if data['know'] == 2: data.setdefault('know', random.randint(1, 2))
    
    if data['know'] == 1:
        #Q4 if downloade == 2, skip to Q11
        data.setdefault('downloaded', random.randint(1, 2))
        #increase the chance of downloaded this game
        if data['downloaded'] == 2: data.setdefault('know', random.randint(1, 2))
        
        if data['downloaded'] == 1:
            #Q5
            data.setdefault('downloadReason', [])
            for i in range(4):
                data['downloadReason'].append(random.randint(0, 1))
            #Q6
            data.setdefault('event', [])
            for i in range(5):
                data['event'].append(random.randint(0, 1))
            #Q7
            data.setdefault('speaker', SPEAKER[random.randint(0, len(SPEAKER)-1)])
            #Q8
            data.setdefault('sEvent', [])
            for i in range(5):
                data['sEvent'].append(random.randint(0, 1))
            #Q9
            data.setdefault('exhibitEvent', random.randint(1, 5))
            #Q10
            data.setdefault('info', [])
            for i in range(6):
                data['info'].append(random.randint(0, 1))
    #Q11*
    data.setdefault('puzzle', random.randint(1, 2))
    #Q12*
    data.setdefault('notDownload', random.randint(1, 5))
    
    #basic data
    #Q1
    data.setdefault('gender', random.randint(1, 2))
    #Q2
    data.setdefault('age', random.randint(1, 5))
    #Q3
    data.setdefault('career', random.randint(1, 5))
    
    return data

def radioBtn(val):
    pyautogui.press('\t')
    if val == 1:
        pyautogui.press(' ')
    else:
        for i in range(1, val): pyautogui.press('down')
            
def checkList(lst):
    for i in range(len(lst)):
        pyautogui.press('\t')
        if lst[i] == 1:
            pyautogui.press(' ')

def filler(data):
    pyautogui.click(170, 200)
    
    #Q1*
    radioBtn(data['spendTime'])
    #Q2*
    pyautogui.press('\t')
    pyautogui.typewrite(data['adPrefer'])
    #Q3* if know == 2, skip to Q11
    radioBtn(data['know'])
    if data['know'] == 1:
        #Q4 if downloade == 2, skip to Q11
        radioBtn(data['downloaded'])
        if data['downloaded'] == 1:
            #Q5
            checkList(data['downloadReason'])
            #Q6
            checkList(data['event'])
            #Q7
            pyautogui.press('\t')
            pyautogui.typewrite(data['speaker'])
            #Q8
            checkList(data['sEvent'])
            #Q9
            radioBtn(data['exhibitEvent'])
            #Q10
            checkList(data['info'])
        else: 
            for i in range(22): pyautogui.press('\t')
    #skip to Q11
    else: 
        for i in range(23): pyautogui.press('\t')
    
    #Q11
    radioBtn(data['puzzle'])
    #Q12
    radioBtn(data['notDownload'])
    
    pyautogui.press('\t')
    pyautogui.press('enter')
    
    time.sleep(2)
    
    #Q1
    radioBtn(data['gender'])
    #Q2
    radioBtn(data['age'])
    #Q3
    radioBtn(data['career'])
    
    pyautogui.press('\t')
    pyautogui.press('\t')
    pyautogui.press('enter')
    time.sleep(2)
    
    #end page
    pyautogui.press('\t')
    pyautogui.press('enter')
    time.sleep(2)
    
if __name__ == '__main__':
    for i in range(30):
        data = generateData()
        print(data)
        print(len(data))
        filler(data)