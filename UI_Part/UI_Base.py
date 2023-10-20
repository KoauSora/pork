import cv2 as cv
import numpy
from PIL import ImageGrab #这个库用来实现截屏的UI
class UI_Base:
    def __init__(self):
        self.image = None
        self.list = None

    def get_mat(self):
        screenshot = ImageGrab.grab()
        numpy_screenshot = numpy.array(screenshot)
        self.image = cv.cvtColor(cv.cvtColor(numpy_screenshot, cv.COLOR_RGB2BGR), cv.COLOR_BGR2GRAY)
        print("Please rewrite this function(UI_Base::get_mat() )!!!")

    def get_ready(self):
        print("Please rewrite this function(UI_Base::get_ready() )!!!")