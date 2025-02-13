import cv2
import numpy as np


#load image and mask
photo_path = './fox-R.png'
mask_path = './fox-m.png'

img = cv2.imread(photo_path)
mask = cv2.imread(mask_path,0)

#inpainting
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

#save inpainted image
cv2.imwrite('./INPAINT_NS algorithm/fox-inpainting.png', dst)


