import cv2
import matplotlib.pyplot as plt

img = cv2.imread('thresholding_otsu\whale.jfif', 0)

thresh_val, thresholed_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

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