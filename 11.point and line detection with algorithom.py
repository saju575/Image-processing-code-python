import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread('line.png',0)

fig=plt.figure(figsize=(7,6))
fig.add_subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.title('Orginal image')
plt.axis('off')

#mux1 for horizontal
mux1=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]],dtype=int)
#mux2 for vertical

mux2=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]],dtype=int)
#mux3 for +45 degree
mux3=np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]],dtype=int)
#mux4 for -45 degree
mux4=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]],dtype=int)

#horizontal line
line1=cv2.filter2D(img, cv2.CV_16S, mux1)
fig.add_subplot(3,3,2)
plt.imshow(line1,cmap='gray')
plt.title('Horizontal')
plt.axis('off')

#vertical line

line2=cv2.filter2D(img, cv2.CV_16S, mux2)
fig.add_subplot(3,3,3)
plt.imshow(line2,cmap='gray')
plt.title('Vatical')
plt.axis('off')

#show addition of vertical and horizontal image
ret, thresh1 = cv2.threshold(cv2.add(line1,line2), 50, 255, cv2.THRESH_BINARY)
fig.add_subplot(3,3,4)
plt.imshow(thresh1,cmap='gray')
plt.title('Vatical+horizontal')
plt.axis('off')


#show 45 degree line
line3=cv2.filter2D(img, cv2.CV_16S, mux3)
fig.add_subplot(3,3,5)
plt.imshow(line3,cmap='gray')
plt.title('45 degree')
plt.axis('off')


# show -45 degree line

line4=cv2.filter2D(img, cv2.CV_16S, mux4)
fig.add_subplot(3,3,6)
plt.imshow(line4,cmap='gray')
plt.title('-45 degree')
plt.axis('off')

#point delection 

p_img=cv2.imread('point.png',0)
fig.add_subplot(3,3,7)
plt.imshow(p_img,cmap='gray')
plt.title('Orginal image')
plt.axis('off')

p_mux=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
p_f_img=cv2.filter2D(p_img, -1, p_mux)
fig.add_subplot(3,3,8)
plt.imshow(p_f_img,cmap='gray')
plt.title('point image')
plt.axis('off')

ret2, thresh2 = cv2.threshold(p_f_img, 100, 255, cv2.THRESH_BINARY)
fig.add_subplot(3,3,9)
plt.imshow(thresh2,cmap='gray')
plt.title('point image')
plt.axis('off')



