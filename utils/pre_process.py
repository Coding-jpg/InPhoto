from PIL import Image

img = Image.open('./test_img_2.jpg')

small_size = (150,150)
resize_img = img.resize(small_size)
resize_img.save('./small_img_2.jpg')