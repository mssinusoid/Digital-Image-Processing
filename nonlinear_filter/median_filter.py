import cv2
import numpy as np
import matplotlib.pyplot as plt

impulse_noise_img = cv2.imread('nonlinear_filter\impulse_noise.png', 0)\

def median_filter(img, n=3):
    h, w = img.shape
    restored_img = np.zeros_like(img)
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
            sorted_neighbors = np.sort(np.array(neighbors))
            restored_img[i, j] = np.median(sorted_neighbors)
    return restored_img

restored_img = median_filter(impulse_noise_img)

plt.axis('off')
plt.subplot(121)
plt.imshow(impulse_noise_img, cmap = "gray")
plt.title('Before')

plt.subplot(122)
plt.imshow(restored_img, cmap = "gray")
plt.title('After')

plt.show()