def imgprocess(imgpath, heavymask,lightmask):
    '''
    input:
    imgpath = full path to image
    returns:
    cloudcover (float from 0-1)
    '''
    #mask=[180,120,120] #bgr
    import cv2

    mask1=[]
    mask2=[]
    masked=0 #pixels

    img=cv2.imread(imgpath)

    print(img.shape[0])
    print(img.shape[1])
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            currentloop=0
            currentcloudtype=('heavy')
            for z in range(img.shape[2]):
                if (img[y,x,z]>=heavymask[z]):
                    currentloop+=1
                    print('2222222-----------')
                else:
                    if (img[y,x,z]>=lightmask[z]):
                        currentcloudtype=('light')
                    else:
                        currentloop=0;break
                    print('this is the case')
            #all the R,G,B values meet the requirements
            if currentloop!=0:
                masked+=(currentloop/img.shape[2]) #+=1 to number of pixels masked
                if currentcloudtype==('heavy'):
                    mask1.append([x, y])  # x and y values appended to the list mask1 as a list [x,y] for annotation
                elif currentcloudtype==('light'):
                    mask2.append([x,y])
    return [(masked/(img.shape[0]*img.shape[1])),mask1,mask2]


#for testing ------- ---------------------------
#masked = imgprocess('TaiMoShanMixedLand.jpg')
#print(masked[0])
#print(imgprocess('TaiMoShanMixedLand.jpg'))