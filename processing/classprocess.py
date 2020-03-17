class Process:
    def __init__(self,imgpath): #image path, cloud cover
        self.imgpath=imgpath #imagepath
        self.ccover=int(0) #cloudcover
        self.heavycloudpixels = []
        self.lightcloudpixels = []
    def __str__(self):
        return self.ccover
    def get_imgpath(self):
        return self.imgpath
    def calc_ccover(self):
        import processing
        self.heavycloudpixels = []
        heavymask = [180,120,120] #bgr
        lightmask = [170,90,50] #bgr
        processed = processing.imgprocess(self.imgpath,heavymask,lightmask) # list [ cloud cover, [[x1,y1],[x2,y2],...]
        self.ccover= processed[0]
        self.heavycloudpixels = processed[1] #reading the returned list from 1 to end
        self.lightcloudpixels = processed[2]
        return self.ccover
    def annotate(self):
        '''
        :param pixel: [x,y] (x and y value stored in a list)
        :param color: [r,g,b] (r,g,b stored in a list)
        :return: None
        '''
        #from .annotate import annotate

        self.calc_ccover() #making sure this function is runned beforehand since data from this is needed
        import annotate
        image = cv2.imread(self.imgpath, 1)
        annotatecolorheavy = [155,99,255]
        annotatecolorlight = [200,200,200]

        print(len(self.heavycloudpixels))
        import time
        print('delaying for you to look at the length of self.cloudpixel')
        time.sleep(1)

        def actualannoate(pixels,imager,color):
            for character in pixels:
                print('working')
                x = character[0]
                print(x)
                y = character[1]
                imager = annotate.annotate(imager, color[0], color[1], color[2], x, y)
            return imager

        mimage = actualannoate(self.lightcloudpixels,image,annotatecolorlight) #original , annotating light first since it should cover more areas and avoid overiding the color of the heavy cloud part
        mimage = actualannoate(self.heavycloudpixels,mimage,annotatecolorheavy) #use mutated image = mimage
        cv2.imshow('image',mimage)
        print('ended')
        return mimage




#testing=Process('asc_hksm_h12m50-cropped.jpg')
#testing=Process('test_offical.jpg')
testing = Process('TaiMoShanMixedLand.jpg')
#testing2=Process('test_white2.jpg')
#testing3=Process('test_black.png')
#print(float(testing.calc_ccover())*100)
#print(testing2.calc_ccover())
#print(testing3.calc_ccover())
# for x in range(0,100):
#     for y in range(0,100):
#         testing.annotate([x,y],[92,209,255])
import cv2
#print(testing.calc_ccover())
newimg = testing.annotate()
cv2.imshow('image', newimg)
import time
print('bequick')
#time.sleep(60.0)
print('bequick')
cv2.waitKey(0)
cv2.destroyAllWindows()

