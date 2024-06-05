import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing import image 
import matplotlib.pyplot as plt


# cwd = os.getcwd()
# path_gambar = os.path.join(cwd, '1.png')
# image = cv2.imread(path_gambar)
img = image.load_img('cat.jpg')
plt.imshow(img)
# image = cv2.resize(image, (224, 224))
# image_array = image / 255.0
# np_img = np.array(image)
 
# summarize some details about the image
# print(image.format)
# print(image.size)
# print(image.mode)

# Convert image into vector
# print(np_img)