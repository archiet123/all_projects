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

def getSelector():
	if final > 48 and final < 60:
		selector = 1
		

toRemove = [')']
characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""

img = cv2.imread(f'first_image.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard
whole = plt.imsave("wholecard.jpg", cropped)

column0 = img[260:650, 470:480]#column0 bounds 
#new = plt.imsave("new1.jpg",column1)
column1 = img[260:650, 483:493]#column1 bounds
#new = plt.imsave("new1.jpg",column1)
column2 = img[260:650, 496:506]#column1 bounds
#new = plt.imsave("new2.jpg",column2)

#image = (f'column{index}') 	



for index in range(0,3):
	read = cv2.imread(f"column{index}.jpg")
	show = cv2.imshow("show", read)
	

	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
#	blurred = cv2.GaussianBlur(gray, (11, 11), 0)
#	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
#	erode = cv2.erode(thresh, None, iterations=2)
#	saveErode = plt.imsave(f'eroded{index}.jpg')
#
	minMaxLoc = cv2.minMaxLoc(read)
#
	yRegion = str(minMaxLoc)[27:30]
#	final = yRegion.replace(')', '')
#	selector = getSelector()
#	
#	
	print(f'the size of the image is: {shape}')
#	print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')
	print(f'y region: {yRegion}')
cv2.waitKey(0)
