from PIL import Image, ImageFilter

filename = raw_input('enter image filename to learn: ')

im = Image.open(filename, 'r')

heightToCrop = im.height % 5
widthToCrop = im.width % 5

croppedImage = im.crop((0,0,(im.width - widthToCrop), (im.height - heightToCrop)))
croppedImage.load()
croppedImage.show()
#im.show()

