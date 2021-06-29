from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith(".jpg"):
        print(f)
        print(type(f))

image1 = Image.open('cat.jpg')
image1.save('cat.png')

image2 = Image.open('cat.png')
image2.show()