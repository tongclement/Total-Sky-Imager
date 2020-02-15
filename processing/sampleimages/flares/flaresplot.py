def density(imgpath):
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
    for p in range(0,256):
        bluepixels.append(0)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            bluepixels[img[x,y,1]]+=1
    #print(bluepixels)
    plt.plot(bluepixels)
    plt.xlabel('Color of pixel (0-255)')
    plt.ylabel('count/concentration')
    plt.title('GreenFlares')
    plt.show()
    #plt.pcolormesh(redpixels,bluepixels,label='redblue')
    #plt.xlabel('red')
    #plt.ylabel('blue')
    #plt.title('collation between red and blue')
    #plt.legend()
    #plt.show()
density('flares1.jpeg')
density('flares2.jpeg')
density('flares3.jpeg')
