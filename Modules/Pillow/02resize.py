# from PIL import Image
# import os

# for f in os.listdir("."):
#     if (f=="dragon.jpg"):
#         i = Image.open(f)

#         name = f.split(".")[0]
#         i.thumbnail((600,300))
#         i.save(f"{name}_resized.jpg")
            
# i.show()

from PIL import Image
 
i = Image.open("cat.jpg")
print(i.size)
i.show()

i_new = i.resize((200,100))
print(i_new.size)
i_new.show()

i_new.save("cat_resized.jpg")

# i.save("cat_resized.jpg")