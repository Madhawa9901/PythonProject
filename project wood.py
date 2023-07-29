import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\Project\\image27.jpg",1)
green = cv2.imread("C:\\Users\\Madhawa\\Desktop\\work\\python\\Project\\green1.jpg",1)
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gus1 = cv2.medianBlur(image,15)
sharp1 = cv2.addWeighted(image,2,gus1,-1,0)

gus2 = cv2.GaussianBlur(image,(19,19),0)

mask = cv2.subtract(image,gus2)

height, width = mask.shape
green = cv2.resize(cv2.cvtColor(green,cv2.COLOR_BGR2RGB),(width,height))

out = cv2.bitwise_and(green,green,mask = mask)

sharp2 = cv2.add(image,cv2.multiply(mask,200))

plt.subplot(121)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(out)

plt.show()