def imgprocess(imgpath):
    '''
    input:
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    mask=[150,150,150]
    mask1=[]
    masked=0 #pixels
    import cv2
    img=cv2.imread(imgpath)
    # from matplotlib import pyplot as plt
    # import numpy as np
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            currentloop=0
            for z in range(img.shape[2]):
                if (img[x,y,z]>=mask[z]):
                    currentloop+=1
                else:
                    currentloop=0; break
            #all the R,G,B values meet the requirements
            mask1.append([x, y]) #x and y values appended to the list mask1 as a list [x,y] for annotation
            masked+=(currentloop/img.shape[2]) #+=1 to number of pixels masked
    return [(masked/(img.shape[0]*img.shape[1])),mask1]


#for testing ------- ---------------------------
#masked = imgprocess('TaiMoShanMixedLand.jpg')
#print(masked[0])
#print(imgprocess('TaiMoShanMixedLand.jpg'))