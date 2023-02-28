import numpy as np
import cv2

# load the input images
img1 = cv2.imread("all_projects\raspi\raspi-stuff\001\image1.jpg")
img2 = cv2.imread('all_projects\raspi\raspi-stuff\001\image2.jpg')
print (img1)
# convert the images to grayscale

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()