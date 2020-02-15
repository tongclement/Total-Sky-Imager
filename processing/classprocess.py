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



#testing=Process('asc_hksm_h12m50-cropped.jpg')
testing=Process('test_offical.jpg')
testing2=Process('test_white2.jpg')
testing3=Process('test_black.png')
print(float(testing.calc_ccover())*100)
print(testing2.calc_ccover())
print(testing3.calc_ccover())


