import os

def rename_files(directory_path):
    # Mendapatkan daftar file dalam direktori
    files = os.listdir(directory_path)
    
    # Mengurutkan file berdasarkan nama
    files.sort()
    
    # Mengubah nama file agar urut dari 1 sampai n
    for i, filename in enumerate(files, start=4005):
        new_name = f"{i}.jpg"  # Ganti dengan ekstensi file yang sesuai
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_name))
        print(f"File {filename} diubah menjadi {new_name}")

# Contoh penggunaan
cwd = os.getcwd()
directory_path = os.path.join(cwd, 'Dataset2', 'normal')  # Ganti dengan path direktori yang sesuai
rename_files(directory_path)