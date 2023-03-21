import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(f'imagesToRead/abc123.jpg')#reading init pic




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

column11 = img[310:650, 609:619]
plt.imsave("assets/testing11.jpg", column11)

column12 = img[310:650, 622:632]
plt.imsave("assets/testing12.jpg", column12)

column13 = img[310:650, 635:645]
plt.imsave("assets/testing13.jpg", column13)

column14 = img[310:650, 648:658]
plt.imsave("assets/testing14.jpg", column14)

column15 = img[310:650, 661:671]
plt.imsave("assets/testing15.jpg", column15)

column16 = img[310:650, 674:684]
plt.imsave("assets/testing16.jpg", column16)
