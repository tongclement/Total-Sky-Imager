# # Cloud extraction idea
# Mark pixels within a certain colour range.

import cv2

img = cv2.imread('asc_hksm_h12m50-cropped.jpg')

#img.shape

from matplotlib import pyplot as plt
import numpy as np

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

colour_ranges=[([75,75,100],[255,255,255]),([192,192,192],[255,255,255])]

print(img[0,0])
print(img.shape)
window_name = "Image and result"
for (lower, upper) in colour_ranges:
     lower = np.array(lower, dtype = "uint8")
     upper = np.array(upper, dtype = "uint8")
     mask = cv2.inRange(img, lower, upper)
     masked=0
     output = cv2.bitwise_and(img, img, mask = mask)
     cv2.imshow(window_name, np.hstack([img, output]))
     cv2.waitKey(0)
     cv2.destroyWindow(window_name)






