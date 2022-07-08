from PIL import Image

i = Image.open("mountain.jpg")
i = i.rotate(90) # inputs in degrees

# saving rotated image
i.save("mountain_rotated.jpg")
i.show()