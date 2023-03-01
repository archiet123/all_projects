import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread(f'first_image.jpg')#reading init pic

img = cv2.imread(f'first_image.jpg')
characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
finalString = ""

def getSelector():
	if final > 48 and final < 60:
		selector = 1
		return(selector)
	elif final > 83 and final < 90:
		selector = 2
		return(selector)
	elif final > 119 and final <130:
		selector = 3
		return(selector)	


#sets new images that are to be read
column0 = img[260:650, 470:480]#column0 bounds 
new = plt.imsave("column0.jpg",column0)
column1 = img[260:650, 483:493]#column1 bounds
new = plt.imsave("column1.jpg",column1)
column2 = img[260:650, 496:506]#column1 bounds
new = plt.imsave("column2.jpg",column2)

#loops for amount of saved images
for index in range(0,3):
	read = cv2.imread(f"column{index}.jpg")
	#show = cv2.imshow("show", read)

	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)#makes image gray
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)#blurrs image
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]#
	erode = cv2.erode(thresh, None, iterations=2)#sets any value over 250 to 255, anything under 250 to 0

	minMaxLoc = cv2.minMaxLoc(gray)#getting minmax value of image

	yRegion = str(minMaxLoc)[26:29]#y axis of bright part of image
	Replace = yRegion.replace(' ', '')
	final = int(Replace)#replacing blank values as nothing and setting to an integer
	selector = getSelector()#calling  getSelector
	
	finalString += characters[index]#appending final value to string

	cv2.waitKey(0)

#print("\n")
print(f"The final string is: {finalString}")