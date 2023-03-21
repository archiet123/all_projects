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
from variables import *
os.system('python variables.py')
os.system('python upperRow.py')

print("\n")
#camera = PiCamera()
#camera.rotation = -180

characters = ['0','1','2','3','4','5','6','7','8','9']
aList = ['&', 'a', 'b','c','d','e','f','g','h','i']
bList = ['-','j','k','l','m','n','o','p','q','r']
cList = ['0','/','s','t','u','v','w','x','y','z']
listChoice = []
final_string = ""
blankCounter = 0

def selectList(result):
	if result == 0:
		listChoice = characters
		return listChoice
	elif result > 30 and result < 50:
		listChoice = aList
		return listChoice
	elif result > 60 and result < 86:
		listChoice = bList
		return listChoice
	elif result > 90 and result < 120:
		listChoice = cList
		return listChoice

def getCharacter(final):
	if final > 5 and final < 30:
		selector = 1
		return selector
	elif final > 45 and final < 75:
		selector = 2
		return selector
	elif final > 80 and final < 100:
		selector = 3
		return selector
	elif final > 115 and final < 140:
		selector = 4
		return selector
	elif final > 150 and final < 180:
		selector = 5
		return selector
	elif final > 185 and final < 210:
		selector = 6
		return selector
	elif final > 220 and final < 245:
		selector = 7
		return selector
	elif final > 250 and final < 280:
		selector = 8
		return selector
	elif final > 290 and final < 320:
		selector = 9
		return selector

	#elif final > 330 and final < 350:
	#	selector = 9
	#	return selector
 

img = cv2.imread(f'imagesToRead/abc123.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard


for index in range(0,8):
	topRowImg = (f'upperRowImages/topRow{index}')
	prepare = cv2.imread(f'{topRowImg}.jpg')

	first_gray = cv2.cvtColor(prepare, cv2.COLOR_BGR2GRAY)
	
	first_blurred = cv2.GaussianBlur(first_gray, (11, 11), 0)	
	first_thresh = cv2.threshold(first_blurred, 200, 255, cv2.THRESH_BINARY)[1]	
	first_erode = cv2.erode(first_thresh, None, iterations=2)
	
	
	first_minMaxLoc = cv2.minMaxLoc(first_erode)
	
	first_yRegion = str(first_minMaxLoc)[25:28]	
	result = first_yRegion.replace(')', '')
	#print(f'result: {result}')

	if result == '':
		result = 0
		result = int(result)
		listSelector = selectList(result)
	else:
		result = int(result)
		listSelector = selectList(result)

	






	imageName = (f'assets/testing{index}') # save images as newimage{column index}    	
	read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read

	# cv2.imshow("window", read)
	# cv2.waitKey(0)

	#shape =read.shape	
	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2
	
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]	
	erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
	#cv2.imwrite('eroded.jpg', erode)#saves the eroded image to the directory
	#cv2.imshow('window', erode)
	
	minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode' 	
	
	yRegion = str(minMaxLoc)[25:28]#just gets the Y axis 	
	final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
	
	#print(f'the size of the image is: {shape}')	
	print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')	
	print(f'{imageName}: {final}')

	if final == '':
		final = 0
		#index += -1
		break
	else:	
		final = int(final)
		selector = getCharacter(final)
		final_string+=listSelector[selector]
		print(f"final string: {final_string}")		
		print("\n")

print("\n")
print(f"the punchcard had {index} columns punched")
print(f'The final string is: {final_string}')

	#cv2.waitKey(0)#is used to keep 

