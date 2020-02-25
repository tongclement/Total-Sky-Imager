import cv2
img = cv2.imread('TaiMoShanMixedLand.jpg',1)
cv2.imshow('image', img)
#import time
#time.sleep(60.0)
print('bequick')
cv2.waitKey(0)
cv2.destroyAllWindows()