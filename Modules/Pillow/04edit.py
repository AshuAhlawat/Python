from PIL import Image, ImageFilter

i = Image.open("cat.jpg")

i_bw = i.convert(mode='L')
i_bw.save("cat_bw.jpg")

i_blur = i.filter(ImageFilter.GaussianBlur(6))
i_blur.save("cat_blur.jpg")

i_blur.show()
i_bw.show()

