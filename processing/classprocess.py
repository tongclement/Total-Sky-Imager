class Process:
    def __init__(self,imgpath): #image path, cloud cover
        self.imgpath=imgpath #imagepath
        self.ccover=int(0) #cloudcover
    def __str__(self):
        return self.ccover
    def get_imgpath(self):
        return self.imgpath
    def calc_ccover(self):
        import processing
        self.ccover=processing.imgprocess(self.imgpath)
        return self.ccover
    def annotate(self,pixel,color):
        '''
        :param pixel: [x,y] (x and y value stored in a list)
        :param color: [r,g,b] (r,g,b stored in a list)
        :return: None
        '''
        #from .annotate import annotate
        import annotate
        #import moduletest
        image = cv2.imread(self.imgpath, 1)
        color = [92,209,255]
        for x in range(0, 100):
            for y in range(0, 100):
                #testing.annotate([x, y], [92, 209, 255])
                 image = annotate.annotate(image, color[0], color[1], color[2], x, y)
        return image




#testing=Process('asc_hksm_h12m50-cropped.jpg')
testing=Process('test_offical.jpg')
testing2=Process('test_white2.jpg')
testing3=Process('test_black.png')
#print(float(testing.calc_ccover())*100)
#print(testing2.calc_ccover())
#print(testing3.calc_ccover())
# for x in range(0,100):
#     for y in range(0,100):
#         testing.annotate([x,y],[92,209,255])
import cv2
newimg = testing.annotate([0,0],[92,209,255])
cv2.imshow('image', newimg)
import time
time.sleep(60.0)
print('bequick')
#cv2.waitKey(0)
cv2.destroyAllWindows()

