import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread('leena.png',0)
fig=plt.figure(figsize=(9,9))
fig.add_subplot(3,2,1)
plt.imshow(img,cmap='gray')
plt.title('Orginal img')
plt.axis('off')

#find negative
img_negative=255-img
fig.add_subplot(3,2,2)
plt.imshow(img_negative,cmap='gray')
plt.title('Negative img')
plt.axis('off')

#find log transformation
# Apply log transformation method

c=255/np.log(1+np.max(img))
log_image=c*np.log(1+img)
# float value will be converted to int
log_image=np.array(log_image,dtype=np.uint8)
fig.add_subplot(3,2,3)
plt.imshow(log_image,cmap='gray')
plt.title('log img')
plt.axis('off')

#Gray level slicing with and without background

#taking Thresholding range
T1=100
T2=180
m,n=img.shape
img_thresh_with_back=np.zeros((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        if(100<=img[i][j]<=180):
            img_thresh_with_back[i][j]=255
        else:
            img_thresh_with_back[i][j]=img[i][j]
            

fig.add_subplot(3,2,4)
plt.imshow(log_image,cmap='gray')
plt.title('ThresholdingBack')
plt.axis('off')

img_thresh_with_noback=np.zeros((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        if(100<=img[i][j]<=180):
            img_thresh_with_noback[i][j]=255
        else:
            img_thresh_with_noback[i][j]=0


fig.add_subplot(3,2,5)
plt.imshow(log_image,cmap='gray')
plt.title('ThresholdingNoBack')
plt.axis('off')









