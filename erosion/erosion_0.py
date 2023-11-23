import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('erosion\j.png', 0)

def erode(img):
    # cố định cửa sổ vì muốn truyền thành đối số tuỳ biến thì lại dài
    kernel=np.ones((3,3),np.uint8)
    h, w = img.shape
    erode_img = np.zeros_like(img)
    
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            temp = []
            temp.append([img[i-1,j-1], img[i-1,j], img[i-1,j+1]])
            temp.append([img[i,j-1], img[i,j], img[i,j+1]])
            temp.append([img[i+1,j-1], img[i+1,j], img[i+1,j+1]])
            z = np.array(temp)
            if np.array(temp).all() == kernel.all():
                erode_img[i, j] = 255
    return erode_img 

erode_img = erode(img)

plt.subplot(121)
plt.title('Before')
plt.imshow(img, cmap = 'gray')
plt.axis('off')

plt.subplot(122)
plt.title('After')
plt.imshow(erode_img, cmap = 'gray')
plt.axis('off')

plt.show()