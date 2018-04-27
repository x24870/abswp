
import cv2
import numpy as np
from PIL import ImageGrab

def get_frame():
    frame = ImageGrab.grab()
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

class Chef():
    def __init__(self):
        self.order_lst = []
        #食材清單
    
    def __str__(self):
        return str(self.order_lst)
    
    def make_onogiri(self):
        pass
    


if __name__ == '__main__':
    chef = Chef()
    print(chef)
