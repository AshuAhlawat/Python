from PIL import Image, ImageFilter

i = Image.open("cat.jpg")
# there are different types of filters available
# the number inside the Gaussian Blur decides the 
# strength of the blur
i_blur = i.filter(ImageFilter.GaussianBlur(6))
i_blur.save("cat_blur.jpg")
i_blur.show()