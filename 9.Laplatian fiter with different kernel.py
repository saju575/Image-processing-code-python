import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import log10,sqrt

img=cv2.imread('leena.png',0)

fig=plt.figure(figsize=(9,9))
fig.add_subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title("Original Img")

#MSE function

# def mse(compressedImg):
#     mse=np.mean((img-compressedImg)**2)
#     if(mse==0):
#         return 100
#     return mse

# #PSNR function

# def psnr(compressedImg):
#     return 20* log10(255/sqrt(mse(compressedImg)))

# #snr function 
# def snr(compressedImg):
#     return 20* log10(np.sum(img**2,dtype = np.float32)/np.sum((img-compressedImg)**2,dtype = np.float32))


g=1
for k in range(3,17,2):
    img_new=cv2.Laplacian(img, ddepth=cv2.CV_64F,ksize=k)
    g=g+1
    # m=mse(img_new)
    # p=psnr(img_new)
    # s=snr(img_new)
    # print("MSE of kernel "+str(k)+" by "+str(k)+" image : "+str(m))
    # print("SNR of kernel "+str(k)+" by "+str(k)+" image : "+str(s))
    # print("PSNR of kernel "+str(k)+" by "+str(k)+" image : "+str(p))
    fig.add_subplot(3,3,g)
    plt.imshow(img_new,cmap='gray')
    plt.axis('off')
    plt.title("Mask size "+str(k))
    
    


