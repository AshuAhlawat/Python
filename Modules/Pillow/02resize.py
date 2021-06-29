from PIL import Image
import os

for f in os.listdir("."):
    if (f=="dragon.jpg"):
        i = Image.open(f)

        name = f.split(".")[0]
        i.thumbnail((600,300))
        i.save("{}_resized.jpg".format(name))
            
            
i.show()
        