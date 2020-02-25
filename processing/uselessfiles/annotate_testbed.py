import cv2
img = cv2.imread('test_white2.jpg',1)
for x in range (0,100):
    for y in range(0,100):
        img = cv2.line(img,(x,y),(x,y),(92,209,255),1)
    print('working')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
