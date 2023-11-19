import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread('histogram_equalization/low_contrast.jpg', 0)

equ = cv2.equalizeHist(gray)

bins = np.arange(256)

plt.subplot(221)
plt.title('Before')
plt.hist(gray.flatten(), bins)

plt.subplot(222)
plt.title('After')
plt.hist(equ.flatten(), bins)

plt.subplot(223)
plt.imshow(gray, cmap="gray")

plt.subplot(224)
plt.imshow(equ, cmap="gray")

plt.show()