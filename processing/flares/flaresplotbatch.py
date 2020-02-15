def density(imgpath):
    '''
    input:
    imgpath = [full path to image1, fpti2]
    returns:
    scattergraph with mattpliot
    '''
    import cv2
    import matplotlib.pyplot as plt
    for n in imgpath:
        img=cv2.imread(n)
        # from matplotlib import pyplot as plt
        # import numpy as np
        redpixels=[]
        greenpixels=[]
        bluepixels=[]
        for p in range(0,256):
            bluepixels.append(0)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                bluepixels[img[x,y,2]]+=1
        #print(bluepixels)
        plt.plot(bluepixels,'b')
        plt.xlabel('Color of pixel (0-255)')
        plt.ylabel('count/concentration')
        plt.title('BlueFlares')
        plt.show()
        #green
        for p in range(0,256):
            greenpixels.append(0)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                greenpixels[img[x,y,1]]+=1
        plt.plot(greenpixels, 'g')
        plt.xlabel('Color of pixel (0-255)')
        plt.ylabel('count/concentration')
        plt.title('GreenFlares')
        plt.show()
        #red
        for p in range(0,256):
            redpixels.append(0)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                redpixels[img[x,y,0]]+=1
        plt.plot(redpixels,'r')
        plt.xlabel('Color of pixel (0-255)')
        plt.ylabel('count/concentration')
        plt.title('RedFlares')
        plt.show()
        #plt.pcolormesh(redpixels,bluepixels,label='redblue')
        #plt.xlabel('red')
        #plt.ylabel('blue')
        #plt.title('collation between red and blue')
        #plt.legend()
        #plt.show()
density(['flares1.jpeg'])
#density('flares2.jpeg')
#density('flares3.jpeg')
