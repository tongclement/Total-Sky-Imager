class Process:
    def __init__(self,imgpath,ccover): #image path, cloud cover
        self.imgpath=imgpath #imagepath
        self.ccover=ccover #cloudcover
    def __str__(self):
        return self.ccover
    def get_imgpath(self):
        return self.imgpath
    def calc_ccover(self):
        import processing
        