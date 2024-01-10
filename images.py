from PIL import Image, ImageFilter

# img = Image.open('./image.jpg')
# # filetered_img = img.filter(ImageFilter.SMOOTH)
# filetered_img = img.convert('L')
# print(img)
# filetered_img.save('grey.png', 'png')
# filetered_img.show()

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')