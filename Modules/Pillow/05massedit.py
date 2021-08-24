from PIL import Image
import os


u_dir = "C:/Users/ashua/OneDrive/Pictures/cell_images/Parasitized/"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+i)
    i = i.resize((64,64))
    i.save("C:/Users/ashua/OneDrive/Pictures/cell_images_n/infected/"+str(x)+".png")
    
u_dir = "C:/Users/ashua/OneDrive/Pictures/cell_images/Uninfected/"
files = os.listdir(u_dir)

x = 0
for i in files:
    x += 1 
    i = Image.open(u_dir+i)
    i = i.resize((64,64))
    i.save("C:/Users/ashua/OneDrive/Pictures/cell_images_n/uninfected/"+str(x)+".png")