def imgprocess(imgpath):
    '''
    input:
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    mask=[255,255,255]
    mask1=[]
    masked=0 #pixels
    import cv2
    img=cv2.imread(imgpath)
    # from matplotlib import pyplot as plt
    # import numpy as np
    print(img.shape[0])
    print(img.shape[1])
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            currentloop=0
            for z in range(img.shape[2]):
                if (img[y,x,z]>=mask[z]):
                    currentloop+=1
                    print('2222222-----------')
                else:
                    currentloop=0;break
                    print('this is the case')
            #all the R,G,B values meet the requirements
            if currentloop!=0:
                masked+=(currentloop/img.shape[2]) #+=1 to number of pixels masked
                mask1.append([x, y])  # x and y values appended to the list mask1 as a list [x,y] for annotation
    return [(masked/(img.shape[0]*img.shape[1])),mask1]


#for testing ------- ---------------------------
#masked = imgprocess('TaiMoShanMixedLand.jpg')
#print(masked[0])
#print(imgprocess('TaiMoShanMixedLand.jpg'))