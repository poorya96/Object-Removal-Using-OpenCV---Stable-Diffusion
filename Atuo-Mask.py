import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

start = time.time()
threshold = 0.9  

# Load images
img = cv2.imread('fox .jpg')  # Original image
imageG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('fox-t.jpg', 0)  # Template image (cropped fox)
w, h = template.shape[::-1]

# Template matching
res = cv2.matchTemplate(imageG, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(res >= threshold)

# Create mask
mask = np.zeros_like(imageG)
for pt in zip(*loc[::-1]):
   cv2.rectangle(mask, (pt[0]-20, pt[1]-20), (pt[0]+w+20, pt[1]+h+20), 255, -1)



##inpainting
image_no_fox = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

end = time.time()
print("Processing Time:", end - start)

# Show results using matplotlib
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(image_no_fox, cv2.COLOR_BGR2RGB))
plt.title("Inpainted Image")
plt.axis("off")

plt.show()