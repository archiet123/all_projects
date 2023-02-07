import numpy as np
import cv2
from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2
camera = PiCamera()
camera.rotation = -180


camera.capture(f'/home/pi/Documents/pi programming/raspi/raspi-stuff/001/first_image.jpg')#taking init pic
img = cv2.imread(f'first_image.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard

#saving the whole punchcard as jpeg
whole = plt.imsave("wholecard.jpg", cropped)

#setting bounds of each column
#to test each column bound save the image look how accurate it is, imshow does not work
#saving the "pre defined" images are called 'column(indexValue). Once they have been defined the name of the images to be saved as must be changed to newimage(indexValue).

column0 = img[260:650, 470:480]#column0 bounds  
zero = plt.imsave("newimage0.jpg", column0)

column1 = img[260:650, 483:493]#column1 bounds
one = plt.imsave("newimage1.jpg", column1)

column2 = img[260:650, 496:506]#column1 bounds
one = plt.imsave("newimage2.jpg", column2)


#--------------the loop-----------------#
def mse(charImage, ogImage):
   h, w = charImage.shape
   diff = cv2.subtract(charImage, ogImage)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

global number
charIndex = 0
characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string = ""
#for loop loops 6 times in testing, will have to be 26 times in practice (PER CHARACTER). 26*86 loops maximum
#(26 per character in alphabet,   86 or x amount for however many holes have been punched )

for columnsIdx in range (0,1):#(0,85):
    for charIndex in range (0,3):#(0,35):
        ogColumnName = (f'newimage{columnsIdx}') # save images as newimage{column index}
        ogImage = cv2.imread(f'{ogColumnName}.jpg', 0)

        charImage = cv2.imread(f'column{charIndex}.jpg', 0)        
        error, diff = mse(charImage, ogImage)
        print("Image matching Error between the two images:",error)
        

        if error > 0.1:#this needs to be changed to a better treashold, dont know best percentage match without testing.
            print(f'There are no differences in the image: column{charIndex} & {ogColumnName}')
            final_string+=characters[charIndex]
            
    
        else:
            print(f'There are differences in the image: column{charIndex} & {ogColumnName}')
            print(f'{percent}')


print(f"The final string is: {final_string}")