import PIL
import cv2

image = cv2.imread('test.png')
template = cv2.imread("onigiri.png")  
result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
print(result)
#print np.unravel_index(result.argmax(),result.shape)

#print(pyautogui.position())