def annotate(image,r,g,b,x,y):
    '''
    :param imagepth:
    :param r:
    :param g:
    :param b:
    :param x:
    :param y:
    :return:
    '''
    print('hey I arrived')
    import cv2
    #image = cv2.imread(imagepth,1)
    endx = x+1
    endy = y+1
    imager = image
    #counting = 0
    #for a in range(x,endx):
     #   counting+=1
      #  print(counting)
       # for b in range(y,endy):
    imager = cv2.line(imager, (x, y), (endx, endy), (b,g,r), 1)
            #print(image==imager)
    #print('I arrived')
        #if counting%10 == 0:
            #cv2.imshow('image', imager)
            #cv2.destroyAllWindows()
    return imager

#import cv2
#tbimg = cv2.imread('test_white2.jpg')
#annotate(tbimg,92,209,255,100,100)
#import cv2
#img=cv2.imread('test_black.png',1)
# imager = cv2.imread('test_offical.jpg',1)
# x= 0
# y = 0
# r = 200
# g = 200
# b = 200
# for x in range (0,100):
#     for y in range(0,100):
#         img = cv2.line(img,(x,y),(x,y),(92,209,255),1)
# for a in range(x, x + 10):
#     for b in range(y, y + 10):
#         imager = cv2.line(imager, (a, b), (a, b), (r, g, b), 1)
# print(imager)
# cv2.imshow('image',img)
# import time
# time.sleep(120.0)
# print('bequick')
# ##cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# img = cv2.imread('test_offical.jpg', 1)
# a=50
# b=50
# endx = a
# endy = b
# for x in range (a,endx):
#     for y in range(b,endy):
#         img = cv2.line(img,(x,y),(x,y),(92,209,255),1)
#     print('working')
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
