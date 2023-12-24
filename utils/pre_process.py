from PIL import Image
import os
from utils.decorators import log
# from decorators import log
import time

@log
def downscale(img_path:str, scale:tuple, res_dir:str) -> str:
    '''
    downscale to scale, img_path is the path of origin img,
    res_path is the downscaled img dir.(without file name)
    '''
    img = Image.open(img_path)
    resize_img = img.resize(scale)
    result_name = 'result_' + str(time.time()) + '.jpg'
    save_path = os.path.join(res_dir, result_name)
    resize_img.save(save_path)

    return save_path

if __name__ == '__main__':
    downscale('../input/test_img_1.jpg', (150,150), '../result/')