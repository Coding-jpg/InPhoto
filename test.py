from PIL import Image, ImageEnhance, ImageFilter

class Photogragh():
    '''
    Load configure, process the single image with configure.
    '''
    def __init__(self, config:dict) -> None:
        self.config = config

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
        if self.config['Blurness'] is not None:
            img = img.filter(ImageFilter.GaussianBlur(radius=self.config['Blurness']))

        # Convert
        if self.config['Convert'] is not None:
            img = img.convert('L')

        return img
    
if __name__ == "__main__":
    config = {'Saturation':1.1, 'Contrast':1.1, 'Brightness':1.05, 'Blurness':None, 'Convert':None}
    photogragher = Photogragh(config=config)  
    result_img = photogragher.params_process(img_path='./test_img_2.jpg')
    result_img.save('./relax_1.jpg')