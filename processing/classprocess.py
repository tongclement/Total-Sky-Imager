class Process:
    def __init__(self,imgpath): #image path, cloud cover
        self.imgpath=imgpath #imagepath
        self.ccover=int(0) #cloudcover
        self.cloudpixels = []
    def __str__(self):
        return self.ccover
    def get_imgpath(self):
        return self.imgpath
    def calc_ccover(self):
        import processing
        processed = processing.imgprocess(self.imgpath) # list [ cloud cover, [[x1,y1],[x2,y2],...]
        self.ccover= processed[0]
        self.cloudpixels = processed[1] #reading the returned list from 1 to end
        return self.ccover
    def annotate(self):
        '''
        :param pixel: [x,y] (x and y value stored in a list)
        :param color: [r,g,b] (r,g,b stored in a list)
        :return: None
        '''
        #from .annotate import annotate

        self.calc_ccover() #making sure this function is runned beforehand since data from this is needed
        print(self.calc_ccover())
        print(self.cloudpixels)
        import annotate
        #import moduletest
        image = cv2.imread(self.imgpath, 1)
        color = [155,99,255]

        print('arriveds')
        print(len(self.cloudpixels
                  ))
        imager = image
        for character in self.cloudpixels:
            print('working')
            x = character[0]
            print(x)
            y = character[1]
            imager = annotate.annotate(imager, color[0], color[1], color[2], x, y)
            #print(image == imager)
        #for x in range(0, 100):
         #   for y in range(0, 100):
                #testing.annotate([x, y], [92, 209, 255])
        cv2.imshow('image',imager)
        print('ended')
        return imager




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

