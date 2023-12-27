from PIL import Image
import os
from utils.decorators import log
# from decorators import log
import time

@log
def downscale(img:Image, scale:tuple) -> str:
    '''downscale to scale, img_path is the path of origin img'''
    resize_img = img.resize(scale)
    return resize_img

if __name__ == '__main__':
    downscale('../input/test_img_1.jpg', (150,150), '../result/')