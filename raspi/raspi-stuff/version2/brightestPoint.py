import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
#camera = PiCamera()
#camera.rotation = -180


img = cv2.imread(f'first_image.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard

whole = plt.imsave("wholecard.jpg", cropped)


column0 = img[260:650, 470:480]#column0 bounds  
zero = plt.imsave("newimage0.jpg", column0)

column1 = img[260:650, 483:493]#column1 bounds
one = plt.imsave("newimage1.jpg", column1)

column2 = img[260:650, 496:506]#column1 bounds
one = plt.imsave("newimage2.jpg", column2)


shape =column1.shape
gray = cv2.cvtColor(column1, cv2.COLOR_BGR2GRAY)
minMaxLoc = cv2.minMaxLoc(gray)
yRegion = str(minMaxLoc)[27:30]#the second value in squre brackets '30' will sometimes return a bracket, find a method to strip this character.

print(f'the size of the image is: {shape}')
print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')
print(f'y region: {yRegion}')

