import numpy as np
import cv2
import matplotlib.pyplot as plt

def equal_hist(img):
    hist = cv2.calcHist([img],[0],None,[256],ranges=[0,256])
    
    m, n = img.shape[:2]
    pdf = hist / (m*n)

    cdf = np.cumsum(pdf)

    s = np.round(255*cdf).astype("uint8")

    equ = np.zeros_like(img)
    equ = s[img]

    return equ

gray = cv2.imread('histogram_equalization/low_contrast.jpg', 0)

equ = equal_hist(gray)

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