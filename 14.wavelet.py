import pywt
from matplotlib import pyplot as plt
import numpy as np
import cv2
if __name__=="__main__":
 def main():
    img=cv2.imread("leena.png")
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=np.float32(img)
    img/=255
    titles=['LL1','LH1','HL1','HH1']
    coeff=pywt.dwt2(img,'db2')
    ll,(lh,hl,hh)=coeff
    plt.figure(figsize=(8,6))
    images=[ll,lh,hl,hh]

    coeff1=pywt.dwt2(ll,'db2')
    ll1,(lh1,hl1,hh1)=coeff1
    images1=[ll1,lh1,hl1,hh1]
    
    titles2=['LL2','LH2','HL2','HH2']

    for i in range(4):
            plt.subplot(2,4,i+1)
            plt.imshow(images[i],cmap='gray')  
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
    
    
    for i in range(4):
            plt.subplot(4,4,i+8+1)
            plt.imshow(images1[i],cmap='gray')  
            plt.title(titles2[i])
            plt.xticks([])
            plt.yticks([])
    #plt.suptitle("For level 2")
    
main()


