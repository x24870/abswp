import cv2

#dict1 = {'a':1, 'b':2}
#
#for i, v in dict1.items():
#    print(i, v)

im = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
print(type(im))
