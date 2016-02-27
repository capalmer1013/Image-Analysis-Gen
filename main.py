from PIL import Image, ImageFilter
import analyze

filename = raw_input('enter image filename to learn: ')

im = Image.open(filename, 'r')

heightToCrop = im.height % 5
widthToCrop = im.width % 5

croppedImage = im.crop((0, 0, (im.width - widthToCrop), (im.height - heightToCrop)))
croppedImage.load()
for i in range(0, croppedImage.height, 5):
    for j in range(0, croppedImage.width, 5):
        analyze.analyzeSquare(croppedImage.crop((j, i, j + 5, i + 5)))


croppedImage.show()
#im.show()

