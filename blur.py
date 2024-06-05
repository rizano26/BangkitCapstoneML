import os
import cv2

cwd = os.getcwd()

    # Path ke gambar
path_gambar = os.path.join(cwd, 'test6060Normal.jpg') #path sebelum melakukan blur (sekarang diganti normal)

    # Membaca gambar
img = cv2.imread(path_gambar)

    # Memeriksa apakah gambar berhasil dibaca
if img is None:
    print(f"Tidak dapat membaca gambar dari path: {path_gambar}")
    print("Pastikan path ke gambar benar dan gambar tidak rusak.")
else:
        # Mendefinisikan ukuran kernel untuk blurring
    kernel_size = (5, 5)

        # Menerapkan Gaussian blurring
    blurred_img = cv2.GaussianBlur(img, kernel_size, 0)

        # Menampilkan gambar asli dan gambar yang sudah di blur
        # cv2.imshow("Gambar Asli", img)
    path_simpan = os.path.join(cwd, 'test6060Blur.jpg') 
    cv2.imwrite(path_simpan, blurred_img)
    print(f"Gambar yang di-blur telah disimpan di: {path_simpan}")