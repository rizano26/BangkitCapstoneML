import os
import cv2

cwd = os.getcwd()

# Path ke gambar
path_gambar = os.path.join(cwd, 'Dataset', 'normal') # path sebelum melakukan blur (sekarang diganti normal)

# # Membaca gambar
# img = cv2.imread(path_gambar)

# # Memeriksa apakah gambar berhasil dibaca
# if img is None:
#     print(f"Tidak dapat membaca gambar dari path: {path_gambar}")
#     print("Pastikan path ke gambar benar dan gambar tidak rusak.")
# else:
#     # Mendefinisikan ukuran kernel untuk blurring
#     kernel_size = (25, 25)

#     # Menerapkan Gaussian blurring
#     blurred_img = cv2.GaussianBlur(img, kernel_size, 0)

#     # Path untuk menyimpan gambar yang di-blur
#     path_simpan_blur = os.path.join(cwd, 'speakerBlur.jpg') 
#     cv2.imwrite(path_simpan_blur, blurred_img)
#     print(f"Gambar yang di-blur telah disimpan di: {path_simpan_blur}")
for i in range(1,2907):
    # Melakukan resize gambar menjadi ukuran 5x5
    img = os.path.join(path_gambar, f'{i}.jpg')
    resized_img = cv2.resize(img, (60, 80))

    # Path untuk menyimpan gambar yang di-resize
    path_simpan_resize = path_gambar
    cv2.imwrite(filename=path_simpan_resize, img=resized_img)
    print(f"Gambar yang di-blur dan di-resize telah disimpan di: {path_simpan_resize}")
