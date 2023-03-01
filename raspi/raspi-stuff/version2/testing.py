import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread(f'first_image.jpg')#reading init pic

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

for index in range(0,3):
	read = cv2.imread(f"column{index}.jpg")
	#show = cv2.imshow("show", read)

	gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)
	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
	erode = cv2.erode(thresh, None, iterations=2)

	#new = plt.imsave("new.jpg",erode)
	#cv2.imwrite("new.jpg", erode)

	minMaxLoc = cv2.minMaxLoc(gray)

	yRegion = str(minMaxLoc)[26:29]
	Replace = yRegion.replace(' ', '')
	final = int(Replace)		
	selector = getSelector()
	
	finalString += characters[index]	

	cv2.waitKey(0)

#print("\n")
print(f"The final string is: {finalString}")