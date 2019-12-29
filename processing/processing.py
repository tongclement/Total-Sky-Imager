def imgprocess(imgpath):
    '''
    input: 
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    mask=[200,200,200]
    masked=0 #pixels
    import cv2
    img=cv2.imread(imgpath)
    #from matplotlib import pyplot as plt
    #import numpy as np
    #print(img[311,195])
    #print(img.shape[2])
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            for z in range(3):
                if (img[x,y,z]>=mask[z]):  masked+=1
    return masked

print(imgprocess('asc_hksm_h12m50-cropped.jpg'))