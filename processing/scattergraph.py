def scatter(imgpath):
    '''
    input:
    imgpath = full path to image
    returns:
    scattergraph with mattpliot
    '''
    import cv2
    import matplotlib.pyplot as plt
    img=cv2.imread(imgpath)
    # from matplotlib import pyplot as plt
    # import numpy as np
    redpixels=[]
    greenpixels=[]
    bluepixels=[]
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            redpixels.append(img[x,y,0])
            greenpixels.append(img[x, y, 1])
            bluepixels.append(img[x, y, 2])
            print('working')
    plt.scatter(redpixels,bluepixels,label='redblue')
    plt.xlabel('red')
    plt.ylabel('blue')
    plt.title('collation between red and blue')
    plt.legend()
    plt.show()
scatter('bluewhitecropped.jpg')