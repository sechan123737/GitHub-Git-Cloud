import numpy as np

gambar = np.array([
    [0, 50, 100],
    [150, 200, 255],
    [30, 80, 180]
])

print("Gambar:")
print(gambar)

print("Ukuran gambar:")
print(gambar.shape)

print("Pixel pertama:")
print(gambar[0][0])

print("Semua pixel:")

for baris in gambar:
    for pixel in baris:
        print(pixel)