from PIL import Image

# just opening an image by it's path
# if image is in the same folder 
# we can just write its name  
img1 = Image.open('./cat.jpg')
img2 = Image.open('./mountain.jpg')
# we can use the img object we created to perform operations
img1.show()
# img2.show()
# we can also save the image using a different name or extension
img1.save('kitty.png')



# import os
# for f in os.listdir('.'):
#     if f.endswith(".jpg"):
#         print(f)
#         print(type(f))