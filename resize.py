import os
import cv2

cwd = os.getcwd()

path_gambar = os.path.join(cwd, 'speaker.jpg') #path sebelum melakukan blur (sekarang diganti normal)

# Membaca gambar
img = cv2.imread(path_gambar)

# Melakukan resize gambar menjadi ukuran 5x5
resized_img = cv2.resize(img, (60, 80))

# Path untuk menyimpan gambar yang di-resize
path_simpan_resize = os.path.join(cwd, 'speakerResized.jpg')
cv2.imwrite(path_simpan_resize, resized_img)
print(f"Gambar yang di-blur dan di-resize telah disimpan di: {path_simpan_resize}")