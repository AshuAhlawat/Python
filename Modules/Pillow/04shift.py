from PIL import Image,ImageOps, ImageChops

img = Image.open("cat.jpg")
# first we pass the image then the x axis shift and then the y axis shift respectively
img = ImageChops.offset(img, -200, 100)
img.save("cat_offset.jpg")
img.show()