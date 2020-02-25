def annotate(imagepth,r,g,b,x,y):
    '''
    :param imagepth:
    :param r:
    :param g:
    :param b:
    :param x:
    :param y:
    :return:
    '''
    import cv2
    image = cv2.imread(imagepth,1)
    image = cv2.line(image, ((x), (y)), (x, y), (r, g, b), 1)
    #cv2.imshow('image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return None

annotate('test_white2.jpg',92,209,255,100,100)
