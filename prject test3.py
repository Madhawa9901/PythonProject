import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\Project\\image1.jpg",0)
green = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\Project\\green1.jpg",1)

kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#gus1 = cv2.GaussianBlur(image,(61,61),0)
gus1 = cv2.medianBlur(image,15)
sharp1 = cv2.addWeighted(image,2,gus1,-1,0)

gus2 = cv2.GaussianBlur(image,(19,19),0)

mask = cv2.subtract(image,gus2)
opening = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
#mask = cv2.medianBlur(mask,5)
height, width = mask.shape
green = cv2.resize(cv2.cvtColor(green,cv2.COLOR_BGR2RGB),(width,height))

out = cv2.bitwise_and(green,green,mask = mask)

sharp2 = cv2.add(image,cv2.multiply(mask,200))

# plt.subplot(411)
# plt.imshow(image)

# plt.subplot(412)
# plt.imshow(sharp1)

# plt.subplot(413)
# plt.imshow(sharp2)

plt.subplot(121)
plt.imshow(mask,cmap='gray')

plt.subplot(122)
plt.imshow(out)

plt.show()