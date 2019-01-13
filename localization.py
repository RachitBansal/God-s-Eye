from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import cv2

car_image = imread("car.jpg", as_grey=True)
# it should be a 2 dimensional array
print(car_image.shape)

# the next line is not compulsory however, a grey scale pixel
# in skimage ranges between 0 & 1. multiplying it with 255
# will make it range between 0 & 255 (something we can relate better with

gray_car_image = car_image 
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image)
threshold_value = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image > threshold_value
ax2.imshow(binary_car_image, cmap="gray")
plt.show()