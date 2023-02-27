import cv2
import numpy as np

im=cv2.imread('column0.ppm')
g = cv2.imread(im, cv2.COLOR_BGR2GRAY)
a = np.array(g)
print (a.max(), np.unravel_index(a.argmax(), a.shape))
a[188:208,478:498] =255
cv2.imshow('aaa',a)