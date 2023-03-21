import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(f'assets/abcCard.jpg')#reading init pic



column0 = img[180:300, 467:477]#column0 bounds  
plt.imsave("upperRowImages/topRow0.jpg", column0)

column1 = img[180:300, 480:490]#column0 bounds  
plt.imsave("upperRowImages/topRow1.jpg", column1)

column2 = img[180:300, 493:503]#column0 bounds  
plt.imsave("upperRowImages/topRow2.jpg", column2)

column3 = img[180:300, 509:519]
plt.imsave("upperRowImages/topRow3.jpg", column3)

column4 = img[180:300, 522:532]
plt.imsave("upperRowImages/topRow4.jpg", column4)

column5 = img[180:300, 533:543]
plt.imsave("upperRowImages/topRow5.jpg", column5)

column6 = img[180:300, 545:555]
plt.imsave("upperRowImages/topRow6.jpg", column6)

column7 = img[180:300, 558: 568]
plt.imsave("upperRowImages/topRow7.jpg", column7)

column8 = img[180:300, 571: 581]
plt.imsave("upperRowImages/topRow8.jpg", column8)

column9 = img[180:300, 584: 594]
plt.imsave("upperRowImages/topRow9.jpg", column9)

column10 = img[180:300, 596:606]
plt.imsave("upperRowImages/topRow10.jpg", column10)