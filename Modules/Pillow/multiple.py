from PIL import Image, ImageFilter, ImageOps

img = Image.open('./cat.jpg')

# cropping the body area of the cat
img = img.crop((200, 125, 420, 310))
# Blurring the image
img = img.filter(ImageFilter.GaussianBlur(6))
# then mirroring the image
img = ImageOps.mirror(img)
# and converting the image into black and white in the end 
img = img.convert(mode='L')

img.show()