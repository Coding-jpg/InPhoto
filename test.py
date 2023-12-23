from PIL import Image, ImageEnhance, ImageFilter

def enhance_loneliness(image_path):
    # 打开图像
    img = Image.open(image_path)

    # 调整色温，增加蓝色调
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0.5)  # 减少饱和度来给予冷色调

    # 调整对比度，增加图像的戏剧性
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)  # 增加对比度

    # 调整亮度，降低以暗示阴郁
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(0.8)  # 降低亮度

    # 应用轻微模糊，增加梦幻感
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # # 转换成黑白，加强孤独感
    # img = img.convert('L')

    return img

# 使用函数
image_path = "./test_img.jpg"
lonely_image = enhance_loneliness(image_path)

# 保存图像
output_path = "./lonely_image.jpg"
lonely_image.save(output_path)