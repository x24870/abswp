# Waiter's work:
# Identify customer's order

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab

#FOOD_PAT_NAMES = ['onigiri.PNG', 'gunkanMaki.png', 'californiaRoll.png',
#                  'salmonRoll.png']
FOOD_PAT_NAMES = ['onigiri.PNG']

class Seat():
    def __init__(self):
        self.seat = False
        self.order = ''
        
    def __str__(self):
        return str(self.seat)

class Waiter():
    def __init__(self):
        self.patterns = self.load_menu()
        
        self.seats = []        
        for i in range(6): self.seats.append(Seat())
        
    def __str__(self):
        #return str([*self.patterns])
        return str(self.patterns.keys())
    
    def load_menu(self):
        patterns = {}
        
        for pic_name in FOOD_PAT_NAMES:
            food_img = cv2.imread(pic_name, cv2.IMREAD_GRAYSCALE)
            patterns.setdefault(pic_name.split('.')[0], food_img)
        return patterns

    def get_frame(self):
        frame = ImageGrab.grab()
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame

    def search_order(self):
        frame = self.get_frame()
        
        for key, pattern in self.patterns.items():
            w, h = pattern.shape
            threshold = 0.7
            res = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
            
            loc = np.where(res > threshold)
            print(loc)
            for pt in zip(*loc):
                cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), 100, 2)
                
            cv2.imshow('pat', pattern)
            cv2.imshow('capture', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
#        result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
#        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#        top_left = max_loc
#        bottom_right = (top_left[0]+pattern.shape[0], top_left[1]+pattern.shape[1])
#        
#        cv2.rectangle(frame, top_left, bottom_right, 0, 2)
#        plt.subplot(121),plt.imshow(result,cmap = 'gray')
#        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#        plt.subplot(122),plt.imshow(frame,cmap = 'gray')
#        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#    
#        plt.show()
#        
#        print('type:', type(result))
#        print(len(result[0]))
        
if __name__ == '__main__':
    waiter = Waiter()
    print(waiter)
    print(*waiter.seats)
    waiter.search_order()