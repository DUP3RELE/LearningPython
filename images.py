from PIL import Image, ImageFilter

img = Image.open('./image.jpg')
filetered_img = img.filter(ImageFilter.BLUR)
print(img)
filetered_img.save('blur.png', 'png')