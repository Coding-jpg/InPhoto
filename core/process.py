from PIL import Image, ImageEnhance, ImageFilter
from utils.decorators import log

class Photogragh():
    '''
    Load configure, process the single image with configure.
    '''
    def __init__(self, config:dict) -> None:
        self.config = config
        self.img = None

    @log
    def params_process(self, img_path) -> Image:
        img = Image.open(img_path)
        # Saturation
        Sat_enhancer = ImageEnhance.Color(img)
        img = Sat_enhancer.enhance(self.config['Saturation'])

        # Contrast
        Cont_enhancer = ImageEnhance.Contrast(img)
        img = Cont_enhancer.enhance(self.config['Contrast'])

        # Brightness
        Brig_enhancer = ImageEnhance.Brightness(img)
        img = Brig_enhancer.enhance(self.config['Brightness'])

        # Blurness
        if self.config['Blurness'] is True:
            img = img.filter(ImageFilter.GaussianBlur(radius=self.config['Blurness']))

        # Convert
        if self.config['Grayscale'] is True:
            img = img.convert('L')

        # Color channels balance
        if self.config['Grayscale'] is not True:
            r_channel = self.config['RGB'][0]
            g_channel = self.config['RGB'][1]
            b_channel = self.config['RGB'][2]
            print(r_channel,g_channel,b_channel)
            img = self.color_balance_process(img, r_channel, g_channel, b_channel)

        self.img = img

        return img
    
    def color_balance_process(self, img:Image, red=1.0, green=1.0, blue=1.0) -> Image:
        '''set the proportion of rgb channels'''
        r, g, b = img.split()
        
        r = r.point(lambda i: i * red)
        b = b.point(lambda i: i * blue)
        g = g.point(lambda i: i * green)

        result_rgb = Image.merge("RGB", (r,g,b))

        return result_rgb
    
    def save_img(self, result_path:str) -> True:
        self.img.save(result_path)

        return True

if __name__ == "__main__":
    # config = {'Saturation':1.1, 'Contrast':1.1, 'Brightness':1.05, 'Blurness':False, 'Convert':False}
    config = {'Saturation': 0.8, 'Contrast': 0.9, 'Brightness': 0.85, 'Blurness': False, 'Convert': False}
    photogragher = Photogragh(config=config)  
    result_img = photogragher.params_process(img_path='./test_img_2.jpg')
    result_img.save('./painful_1.jpg')