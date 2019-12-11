import numpy as np
import cv2
from matplotlib import pyplot as plt

#load color image in greyscale

pic = cv2.imread("liz.jpg", 0)
plt.imshow (pic,cmap='gray', interpolation = 'bicubic')
#plt.xtics([]), plt.yticks([]), #for hiding x and y axes

plt.show()


#print(pic)
#cv2.imshow('liz.jpg', pic)























