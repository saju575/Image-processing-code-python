import cv2
from matplotlib import pyplot as plt
from math import log10,sqrt
import numpy as np

img=cv2.imread('leena.png',0)

fig=plt.figure(figsize=(9,9))
fig.add_subplot(4,3,1)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title('Orginal Image')
img_new=img
#MSE function

def mse(compressed):
    mse=np.mean((img-compressed)**2)
    if mse==0:
        return 100
    return mse

#SNR function
def snr(compressed):
    return 20*log10(np.sum(img**2,dtype=np.float32)/np.sum((img-compressed)**2,dtype=np.float32))

#PSNR function

def psnr(compressed):
    return 20*log10(255/sqrt(snr(compressed)))


for k in range(10):
    img_new=cv2.blur(img_new, (7,7))
    m=mse(img_new)
    s=snr(img_new)
    p=psnr(img_new)
    print("MSE of kernel "+str(k+1)+" by "+str(k+1)+" image : "+str(m))
    print("SNR of kernel "+str(k+1)+" by "+str(k+1)+" image : "+str(s))
    print("PSNR of kernel "+str(k+1)+" by "+str(k+1)+" image : "+str(p))
    fig.add_subplot(4,3,k+2)
    plt.imshow(img_new,cmap="gray")
    plt.axis('off')
    plt.title(str(k+1)+' times kernel')
    
    


