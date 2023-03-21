import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(f'assets/realTest.jpg')#reading init pic





column0 = img[310:650, 467:477]#column0 bounds  
plt.imsave("assets/testing0.jpg", column0)

column1 = img[310:650, 480:490]#column1 bounds
plt.imsave("assets/testing1.jpg", column1)

column2 = img[310:650, 493:503]#column2 bounds
plt.imsave("assets/testing2.jpg", column2)

column3 = img[310:650, 509:519]
plt.imsave("assets/testing3.jpg", column3)

column4 = img[310:650, 522:532]
plt.imsave("assets/testing4.jpg", column4)

column5 = img[310:650, 533:543]
plt.imsave("assets/testing5.jpg", column5)

column6 = img[310:650, 545:555]
plt.imsave("assets/testing6.jpg", column6)

column7 = img[310:650, 558: 568]
plt.imsave("assets/testing7.jpg", column7)

column8 = img[310:650, 571: 581]
plt.imsave("assets/testing8.jpg", column8)

column9 = img[310:650, 584: 594]
plt.imsave("assets/testing9.jpg", column9)

column10 = img[310:650, 596:606]
plt.imsave("assets/testing10.jpg", column10)

'''
listSelector0 = img[195:310, 470:480]
plt.imsave("assets/first.jpg", listSelector0)

listSelector1 = img[195:310, 470:480]
plt.imsave("assets/second.jpg", listSelector1)

listSelector2 = img[195:310, 470:480]
plt.imsave("assets/third.jpg", listSelector2)
'''