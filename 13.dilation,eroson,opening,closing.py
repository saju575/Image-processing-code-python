import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread('sig.png',0)
ret,bw=cv2.threshold(img, 127, np.max(img), cv2.THRESH_BINARY)
fig=plt.figure(figsize=(9,9))


str_element=np.ones((6,6),np.uint8)
#Performing Erosion Operation
erosion=cv2.erode(bw, str_element,iterations = 1)


#Performing Dilation Operation
dilatedImage=cv2.dilate(bw, str_element,iterations=1)


#opening
img2=cv2.imread('sample.png',0)
kep,img2=cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
openImg=cv2.morphologyEx(img2, cv2.MORPH_OPEN, str_element)

#closing
img3=cv2.imread('c.png',0)
ke,img3=cv2.threshold(img3, 127, 255, cv2.THRESH_BINARY)
closeingImg=cv2.morphologyEx(img3, cv2.MORPH_CLOSE, str_element)

img_arr=[bw,erosion,dilatedImage,img2,openImg,img3,closeingImg]
img_title=['Orginal img','Erosion image','Dilated image','Orginal img',"openingImg",'Orginal img','Closing img']

for k in range(len(img_arr)):
    fig.add_subplot(3,3,k+1)
    plt.imshow(img_arr[k], cmap='gray')
    plt.title(img_title[k])
    plt.axis('off')



