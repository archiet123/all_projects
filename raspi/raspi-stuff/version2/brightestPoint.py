import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
from imutils import contours
#camera = PiCamera()
#camera.rotation = -180



img = cv2.imread(f'first_image.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard

column0 = img[260:650, 470:480]#column0 bounds  


column1 = img[260:650, 483:493]#column1 bounds


column2 = img[260:650, 496:506]#column1 bounds


toRemove = ["/", ")", "("]
All = [""]

for index in range(0,3):
    imageName = (f'column{index}') # save images as newimage{column index}    
	
    read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read
	
    shape =read.shape
	
    gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2    

	
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
	
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
	
    erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image

	#cv2.imwrite('eroded.jpg', erode)#saves the eroded image to the directory
	#cv2.imshow('window', erode)

	
    minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode' 
	
    
    yRegion = str(minMaxLoc)[25:28]#just gets the Y axis 
	
    final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
	
    print(f'the size of the image is: {shape}')
	
    print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')
	
    print(f'y region: {final}')
	
    All.append(final)
	#cv2.waitKey(0)#is used to keep 

print(All)
