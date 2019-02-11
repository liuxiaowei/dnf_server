import sys
import random
import string

from PIL import Image, ImageDraw, ImageFont, ImageFilter


if sys.platform == 'win32':
    font_path = 'C:\\Windows\\Fonts\\arial.ttf'
else:
    font_path = '/usr/share/fonts/arial.ttf'


fontcolor = (255, 255, 255)
linecolor = (0, 0, 255)
draw_line = True


def gen_code(number):
    source = list(string.digits + string.ascii_lowercase)
    return ''.join(random.choice(source) for _ in range(number))


def gen_line(draw, width, height):
    for i in range(random.randint(1, 3)):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=linecolor)


def gen_captcha(width=100, height=100, number=4):
    bgcolor = (255, 0, 0)
    image = Image.new('RGBA', (width, height), bgcolor)  # 创建图片
    font = ImageFont.truetype(font_path, 100)  # 验证码的字体
    draw = ImageDraw.Draw(image)  # 创建画笔
    code = gen_code(number)
    font_width, font_height = font.getsize(code)
    draw.text(((width - font_width) / number, (height - font_height) / number), code,
              font=font, fill=fontcolor)

    if draw_line:
        gen_line(draw, width, height)

    image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强

    return image, code
