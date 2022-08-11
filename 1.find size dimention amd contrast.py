import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

#image read

img=cv2.imread('leena.png',0)

#find dimension
dimension=img.shape

print('Dimension',dimension)
#find size
height=img.shape[0]
width=img.shape[1]
print("Height : ",height," Width : ",width)

#find the value of a particular pixel

print('(1,2) pixel value : ',img[1][2])

#edit a particular pixel

img[1][2]=170
print('(1,2) pixel value : ',img[1][2])

#find the max and min pixel value

maxPixel=np.max(img)
minPixel=np.min(img)
print('MaxPixel: ',maxPixel," MinPixel: ",minPixel)

#find contrast
brightness=np.mean(img)


con2=sqrt(np.sum((img-brightness)**2))
contrast2=sqrt(1/(height*width))*con2
print("Contrast: ",contrast2)

#Display the image repeatedly in 3x 3 tabular format 
fig=plt.figure()
for k in range(9):
    fig.add_subplot(3,3,k+1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    
