import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
from imutils import contours

characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""

def getCharacter(final):
    if final > 48 and final < 60:
        selector = 1
        return selector
    elif final > 79 and final < 90:
        selector = 2
        return selector
    elif final > 113 and final < 130:
        selector = 3
        return selector

img = cv2.imread(f'first_image.jpg')#reading init pic


column0 = img[260:650, 470:480]#column0 bounds
plt.imsave("testing0.jpg", column0)
column1 = img[260:650, 483:493]#column1 bounds
plt.imsave("testing1.jpg", column1)
column2 = img[260:650, 496:506]#column1 bounds
plt.imsave("testing2.jpg", column2)
toRemove = ["/", ")", "("]
for index in range(0,3):
    imageName = (f'testing{index}') # save images as newimage{column index}
    read = cv2.imread(f'{imageName}.jpg')#this will need to loop through all images that need to be read
    #shape =read.shape
    gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) #the first parameter is the image that is read by cv2

    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    erode = cv2.erode(thresh, None, iterations=2) # perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
    minMaxLoc = cv2.minMaxLoc(erode)#minMaxloc finds the darkest and brightest part of the image (varibale) 'erode'
    yRegion = str(minMaxLoc)[25:28]#just gets the Y axis
    final = yRegion.replace(')', '')#replacing the bracket that is returned with tripple digit coords
    print(f'the brightest part of the image, darkest part of the image, x coord, y coord{minMaxLoc}')
    print(f'y region: {final}')
    final = int(final)
    selector = getCharacter(final)
    final_string+=characters[selector]
print("\n")
print(f'The final string is: {final_string}')