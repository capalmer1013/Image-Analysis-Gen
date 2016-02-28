from PIL import Image, ImageFilter
import analyze

filename = raw_input('enter image filename to learn: ')

im = Image.open(filename, 'r')
im = im.convert('P', palette=Image.ADAPTIVE, colors=10)
im.show()

for i in range(0, im.height):
    for j in range(0, im.width):
        try:
            top = im.getpixel((j, i-1))
        except IndexError:
            top = None
        try:
            bottom = im.getpixel((j, i+1))
        except IndexError:
            bottom = None
        try:
            left = im.getpixel((j-1, i))
        except IndexError:
            left = None
        try:
            right = im.getpixel((j+1, i))
        except IndexError:
            right = None

        analyze.analyzePixel(im.getpixel((j, i)), left, top, right, bottom)
