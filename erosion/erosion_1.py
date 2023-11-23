import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('erosion\j.png')

kernel = np.ones((3, 3))
erode_img = cv2.erode(img, kernel)

plt.subplot(121)
plt.title('Before')
plt.imshow(img)
plt.axis('off')

plt.subplot(122)
plt.title('After')
plt.imshow(erode_img)
plt.axis('off')

plt.show()