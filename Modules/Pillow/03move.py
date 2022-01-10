from PIL import Image

i = Image.open("mountain.jpg")
i = i.rotate(90)

i.save("mountain_rotated.jpg")
i.show()