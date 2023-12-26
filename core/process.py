from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
from utils.decorators import log

class Photogragh():
    '''
    Load configure, process the single image with configure.
    '''
    def __init__(self, config:dict) -> None:
        self.config = config
        self.img = None
        self.origin_img = None

    @log
    def params_process(self, img_path:str) -> Image:
        '''Core process function
        Saturation, Contrast, Brightness, Blurness, Convert, Color channels balance
        '''
        self.origin_img = img = Image.open(img_path)
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
    
    def save_img(self, result_path:str, mode:str, prompt:str) -> True:
        if mode == "pure":
            # directly save the result
            self.img.save(result_path)
        elif mode == "compare":
            # concat the origin img and result img, for test
            img_name_1 = 'Origin'
            img_name_2 = prompt
            
            font = ImageFont.load_default()

            max_height = max(self.origin_img.height, self.img.height)
            total_width = self.origin_img.width + self.img.width

            new_image = Image.new('RGB', (total_width, max_height + 50), 'white')
            draw = ImageDraw.Draw(new_image)

            new_image.paste(self.origin_img, (0, 0))
            new_image.paste(self.img, (self.origin_img.width, 0))
            
            text_width1 = draw.textlength(img_name_1, font=font)
            text_x1 = self.origin_img.width // 2 - text_width1 // 2
            draw.text((text_x1, max_height + 10), img_name_1, fill="black", font=font)

            text_width2 = draw.textlength(img_name_2, font=font)
            text_x2 = self.origin_img.width + self.img.width // 2 - text_width2 // 2
            draw.text((text_x2, max_height + 10), img_name_2, fill="black", font=font)

            new_image.save(result_path)

        return True

if __name__ == "__main__":
    # config = {'Saturation':1.1, 'Contrast':1.1, 'Brightness':1.05, 'Blurness':False, 'Convert':False}
    config = {'Saturation': 0.8, 'Contrast': 0.9, 'Brightness': 0.85, 'Blurness': False, 'Convert': False}
    photogragher = Photogragh(config=config)  
    result_img = photogragher.params_process(img_path='./test_img_2.jpg')
    result_img.save('./painful_1.jpg')