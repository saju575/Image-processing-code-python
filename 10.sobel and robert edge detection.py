import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread('leena.png',0)

fig=plt.figure(figsize=(9,9))
fig.add_subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Orginal image')
plt.axis('off')

#soble
soble_img=cv2.Sobel(img, cv2.CV_64F, dx=1, dy=1,ksize=3)
fig.add_subplot(2,2,2)
plt.imshow(soble_img,cmap='gray')
plt.title('Sobel image')
plt.axis('off')

# Roberts operator 

kernelX=np.array([[-1,0],[0,-1]],dtype=int)
kernelY=np.array([[0,-1],[-1,0]],dtype=int)
x=cv2.filter2D(img, cv2.CV_16S, kernelX)
y=cv2.filter2D(img, cv2.CV_16S, kernelY)
roberts=cv2.add(x,y)
roberts=cv2.convertScaleAbs(roberts)
# absX=cv2.convertScaleAbs(x)
# absY=cv2.convertScaleAbs(y)
#roberts=cv2.addWeighted(absX, .5, absY, .5, 0)
# roberts=cv2.add(absX,absY)
fig.add_subplot(2,2,3)
plt.imshow(roberts,cmap='gray')
plt.title('Roberts image')
plt.axis('off')

