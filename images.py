from PIL import Image, ImageFilter

img = Image.open('./image.jpg')
# filetered_img = img.filter(ImageFilter.SMOOTH)
filetered_img = img.convert('L')
print(img)
filetered_img.save('grey.png', 'png')