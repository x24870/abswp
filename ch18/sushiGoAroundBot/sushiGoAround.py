#TODO maybe use multithread to detect pattern?

import cv2, time
import pyautogui
import numpy as np
from PIL import ImageGrab
from matplotlib import pyplot as plt

ONIGIRI_PAT = cv2.imread('onigiri.png', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('11', ONIGIRI_PAT)
print(ONIGIRI_PAT.shape)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#get screen
def get_screen():
    scrImg = ImageGrab.grab()
    npImg = np.array(scrImg)
    frame = cv2.cvtColor(npImg, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', frame)    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return frame

#search custom order
def search_order(frame):
    pattern = ONIGIRI_PAT
    
    result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0]+pattern.shape[0], top_left[1]+pattern.shape[1])
    
    cv2.rectangle(frame, top_left, bottom_right, 0, 2)
    plt.subplot(121),plt.imshow(result,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(frame,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

    plt.show()
    
    print('type:',type(result))
    print(len(result[0]))

#identify food

#make food

#cleaning table

#order ingredients

#Main    
start_time = time.time()
frame = get_screen()
search_order(frame)
print(time.time() - start_time)