from PIL import Image, ImageOps

i = Image.open("cat.jpg")

i_flip = ImageOps.flip(i) 
# saving flipped(vertically) image
i_flip.save("cat_flipped.jpg")
i_flip.show()

i_mir = ImageOps.mirror(i) 
# saving mirrored(horizontally) image
i_mirr.save("cat_mirrored.jpg")
i_mirr.show()