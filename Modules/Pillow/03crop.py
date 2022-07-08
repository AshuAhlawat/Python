from PIL import Image

img = Image.open('./cat.jpg')
# top left of image is 0,0 and we are selecting the x,y coordinates of the top left and bottom right corner of the crop respectively
img = img.crop((200, 200, 300, 300))
img.show()