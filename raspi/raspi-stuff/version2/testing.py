import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
import os

from variables import * #importing variables from other file
os.system('python variables.py')


#camera = PiCamera()
#camera.rotation = -180

characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""

def getCharacter(final):
	if final > 20 and final < 50:
		selector = 0
		return selector
	elif final > 55 and final < 90:
		selector = 1
		return selector
	elif final > 95 and final < 120:
		selector = 2
		return selector
	elif final > 125 and final < 140:
		selector = 3
		return selector
	elif final > 160 and final < 180:
		selector = 4
		return selector
	elif final > 190 and final < 210:
		selector = 5
		return selector
	elif final > 230 and final < 250:
		selector = 6
		return selector
	elif final > 265 and final < 280:
		selector = 7
		return selector
	elif final > 295 and final < 320:
		selector = 8
		return selector
	elif final > 330 and final < 350:
		selector = 9
		return selector

img = cv2.imread(f'assets/card.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard


toRemove = ["/", ")", "("]


for index in range(0,10):
	imageName = (f'assets/testing{index}') # save images as newimage{column index}    	
	read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read

	# cv2.imshow("window", read)
	# cv2.waitKey(0)

	#shape =read.shape	
	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2
	
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]	
	erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
	cv2.imwrite('eroded.jpg', erode)#saves the eroded image to the directory
	#cv2.imshow('window', erode)
	
	minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode' 	
	
	yRegion = str(minMaxLoc)[25:28]#just gets the Y axis 	
	final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
	
	#print(f'the size of the image is: {shape}')	
	print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')	
	print(f'{imageName} {final}')

	if final == '':
		break
	else:	
		final = int(final)
		selector = getCharacter(final)
		final_string+=characters[selector]

print("\n")
print(f"the punchcard had {index} columns punched")
print(f'The final string is: {final_string}')

	#cv2.waitKey(0)#is used to keep 

