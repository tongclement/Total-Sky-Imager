def imgprocess(imgpath):
    '''
    input: 
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    mask=[250,250,250]
    masked=0 #pixels
    import cv2
    img=cv2.imread(imgpath)
    # from matplotlib import pyplot as plt
    # import numpy as np
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            currentloop=0
            for z in range(img.shape[2]):
                if (img[x,y,z]>=mask[z]):currentloop+=1
                else: currentloop=0; break
            masked+=(currentloop/img.shape[2])
    return masked/(img.shape[0]*img.shape[1])

print(imgprocess('asc_hksm_h12m50-cropped.jpg'))