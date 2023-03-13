import cv2
import PIL
import matplotlib.pyplot as plt

img = cv2.imread(f'card.jpg')#reading init pic
cropped = img[260:650,460:1460]#setting bounds of whole punchcard

column0 = img[260:650, 470:480]#column0 bounds  
plt.imsave("testing0.jpg", column0)
column1 = img[260:650, 483:493]#column1 bounds
plt.imsave("testing1.jpg", column1)
column2 = img[260:650, 496:506]#column1 bounds
plt.imsave("testing2.jpg", column2)

column3 = img[260:650, 509:519]
plt.imsave("testing3.jpg", column3)

column4 = img[260:650, 522:532]
plt.imsave("testing4.jpg", column4)

column5 = img[260:650, 533:543]
plt.imsave("testing5.jpg", column5)

column6 = img[260:650, 545:555]
plt.imsave("testing6.jpg", column6)

column7 = img[260:650, 558: 568]
plt.imsave("testing7.jpg", column7)

column8 = img[260:650, 571: 581]
plt.imsave("testing9.jpg", column8)

column9 = img[260:650, 584: 594]
plt.imsave("testing9.jpg", column9)

