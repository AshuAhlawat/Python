from PIL import Image, ImageFilter

i = Image.open("cat.jpg")

# here changing the mode changes the output image color mode
i_bw = i.convert(mode='L')
i_bw.save("cat_bw.jpg")
# i_bw.show()

# this mode kind of pixelates the lines/edges
i_grain = i.convert(mode='1')
i_grain.save("cat_grain.jpg")
i_grain.show()
