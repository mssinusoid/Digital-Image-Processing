import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('thresholding_otsu\whale.jfif', 0)

def otsu(img):
    total_pixels = img.size
    hist, bins = np.histogram(img, bins=np.arange(257))

    opt_thres = -1
    var = -1

    for k in bins[1:-1]:
        p1 = np.sum(hist[:k]) / total_pixels    
        m1 = np.sum(np.arange(k+1) * hist[:k+1]) / np.sum(hist[:k+1])
        m2 = np.sum(np.arange(k+1, 256) * hist[k+1:]) / np.sum(hist[k+1:])
        var_temp = p1 * (1-p1) * (m1-m2)**2

        if var < var_temp:
            var = var_temp
            opt_thres = k

    thresholed_img = img.copy()
    thresholed_img[img > opt_thres] = 255
    thresholed_img[img <= opt_thres] = 0
    return opt_thres, thresholed_img

thresh_val, thresholed_img = otsu(img)

print(thresh_val)

plt.subplot(121)
plt.imshow(img, cmap = "gray")
plt.title('Before')
plt.axis('off')

plt.subplot(122)
plt.imshow(thresholed_img, cmap = "gray")
plt.title('After')
plt.axis('off')

plt.show()