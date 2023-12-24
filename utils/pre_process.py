from PIL import Image

def downscale(img_path:str, scale:tuple) -> None:
    img = Image.open(img_path)
    resize_img = img.resize(scale)
    resize_img.save('./input/small_img_2.jpg')