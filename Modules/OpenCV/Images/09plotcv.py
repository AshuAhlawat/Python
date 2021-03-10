import matplotlib.pyplot as plt
import cv2

image = plt.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\dragon.jpg')
plt.imshow(image)
plt.show()

plt.hist(image.ravel(),bins=30,ec='k')
plt.show()


image = plt.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\cat.jpg')
plt.imshow(image)
plt.show()

plt.hist(image.ravel(),bins=70,ec='k')
plt.show()


image = plt.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\jungle.jpg')
plt.imshow(image)
plt.show()

plt.hist(image.ravel(),fc='k')
plt.show()

image = plt.imread('C:\\Users\\ashua\\OneDrive\\Desktop\\Coding\\Python\\Modules\\OpenCV\\mountain.jpg')
plt.imshow(image)
plt.show()

plt.hist(image.ravel(),bins=256)
plt.show()

hist = cv2.calcHist([image], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()