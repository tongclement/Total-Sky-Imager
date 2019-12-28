def imgprocess(imgpath):
    '''
    input: 
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    mask=[250,250,250]
    masked=0 #pixels
    import cv2 as cv
    img=cv2.imread(imgpath)
    from matplotlib import pyplot as plt
    import numpy as np
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            pixel=img[x,y] #pixel will be [red,green,blue]
            for x in range(img.shape[2]):
                if pixel[x]>mask[x]:
                    masked+=1
    return masked

print(imgprocess('asc_hksm_h12m50-cropped.jpg'))