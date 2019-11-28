class pixel:
    '''
    This class should take in the pixel data
    the calc function decides whether the pixel is part of the cloud or not and returns True or False
            True = is a cloud
            False= is clear
    '''
    def __init__(self,red,blue,green):
        self.red = red
        self.blue = blue
        self.green = green
    def calc(self):
        '''
        the calc method uses the values self.red, self.blue, self.green
        a red blue balance method should be inherited
        :return: True or False
            True = Cloud
            False = Clear
        '''

#random,to be deleated