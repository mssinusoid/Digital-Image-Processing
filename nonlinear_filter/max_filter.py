import cv2
import numpy as np
import matplotlib.pyplot as plt

pepper_noise_img = cv2.imread('nonlinear_filter\pepper_noise.jpg', 0)

def max_filter(img, n=3):
    h, w = img.shape
    restored_img = np.copy(img)
    for i in range(h-n//2):
        for j in range(w-n//2):
            neighbors = [img[i,j]]
            for s in range(1, (n//2)+1):
                neighbors.append(img[i-s,j-s])
                neighbors.append(img[i-s,j])
                neighbors.append(img[i-s,j+s])
                neighbors.append(img[i,j-1])
                neighbors.append(img[i,j+1])
                neighbors.append(img[i+s,j-s])
                neighbors.append(img[i+s,j])
                neighbors.append(img[i+s,j+s])
            restored_img[i, j] = max(neighbors)
    return restored_img

restored_img = max_filter(pepper_noise_img)

plt.subplot(121)
plt.title('Before')
plt.imshow(pepper_noise_img, cmap = "gray")
plt.axis('off')

plt.subplot(122)
plt.title('After')
plt.imshow(restored_img, cmap = "gray")
plt.axis('off')

plt.show()