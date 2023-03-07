import cv2
import PIL
import matplotlib.pyplot as plt
import cv2


img = cv2.imread(f'first_image.jpg')

column0 = img[260:650, 580:590]#column0 bounds  
plt.imsave("testing3.jpg", column0)
read = cv2.imread("testing3.jpg")

gray = cv2.cvtColor(read, cv2.COLOR_BGR2GRAY) 
	
blurred = cv2.GaussianBlur(gray, (11, 11), 0)	
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]	
erode = cv2.erode(thresh, None, iterations=2)

minMaxLoc = cv2.minMaxLoc(erode)
print(minMaxLoc)