import os
import cv2

cwd = os.getcwd()

# Path ke folder yang berisi gambar
path_gambar = os.path.join(cwd, 'Dataset', 'normal') # path sebelum melakukan blur (sekarang diganti normal)

# Loop untuk membaca, resize, dan menyimpan gambar
for i in range(1, 2907):
    # Path lengkap ke gambar
    img_path = os.path.join(path_gambar, f'{i}.jpg')
    
    # Membaca gambar
    img = cv2.imread(img_path)
    
    # Memeriksa apakah gambar berhasil dibaca
    if img is None:
        print(f"Tidak dapat membaca gambar dari path: {img_path}")
        continue
    
    # Melakukan resize gambar menjadi ukuran 60x80
    resized_img = cv2.resize(img, (60, 80))
    
    # Path untuk menyimpan gambar yang di-resize
    path_simpan_resize = os.path.join(path_gambar, f'resized_{i}.jpg')
    cv2.imwrite(path_simpan_resize, resized_img)
    print(f"Gambar yang di-resize telah disimpan di: {path_simpan_resize}")
