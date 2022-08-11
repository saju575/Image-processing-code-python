import cv2
from matplotlib import pyplot as plt

img=cv2.imread('leena.png')
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img0=img&1
img1=img&2
img2=img&4
img3=img&8
img4=img&16
img5=img&32
img6=img&64
img7=img&128
compressed=img&248

images=[img0,img1,img2,img3,img4,img5,img6,img7,compressed]
titles=['1th bit plane','2nd bit plane','3rd bit plane','4th bit plane','5th bit plane','6th bit plane','7th bit plane','8th bit plane','Compressed Image']

fig=plt.figure(figsize=(9,9))
fig.add_subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title('Main image')
plt.axis('off')

g=1
lists=[1,6,8]
for k in range(3):
    g=g+1
    fig.add_subplot(2,2,g)
    
    plt.imshow(images[lists[k]],cmap='gray')
    plt.title(titles[lists[k]])
    plt.axis('off')
    
print('Compression ratio: ',(8/5))
    

