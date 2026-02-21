import cv2
import numpy as np
import math

# ===============================
# 1. Membaca Gambar
# ===============================
img = cv2.imread("Basko.jpeg")

if img is None:
    print("Gambar tidak ditemukan!")
    exit()

height, width, channels = img.shape

print("===== INFORMASI DASAR CITRA =====")
print(f"Resolusi Spasial      : {width} x {height} piksel")
print(f"Jumlah Channel Warna  : {channels} (BGR)")
print("Artinya gambar ini adalah citra berwarna (RGB/BGR).")

# ===============================
# 2. Bit Depth
# ===============================
bit_depth_per_channel = 8
total_bit_depth = bit_depth_per_channel * channels
jumlah_warna = 2 ** total_bit_depth

print(f"\nBit Depth per Channel : {bit_depth_per_channel} bit")
print(f"Total Bit Depth       : {total_bit_depth} bit")
print(f"Jumlah Warna Teoritis : {jumlah_warna:,} warna")

# ===============================
# 3. Aspect Ratio
# ===============================
gcd = math.gcd(width, height)
aspect_width = width // gcd
aspect_height = height // gcd

print(f"\nAspect Ratio          : {aspect_width}:{aspect_height}")

# ===============================
# 4. Ukuran Memori Teoritis
# ===============================
memory_bytes = width * height * total_bit_depth / 8
memory_kb = memory_bytes / 1024
memory_mb = memory_kb / 1024

print(f"\nUkuran Memori Teoritis:")
print(f"{memory_bytes:,.0f} Bytes")
print(f"{memory_kb:.2f} KB")
print(f"{memory_mb:.2f} MB")

# ===============================
# 5. Simulasi Perubahan
# ===============================
new_width = width * 2
new_height = height * 2
new_bit_depth = total_bit_depth // 2

new_memory = new_width * new_height * new_bit_depth / 8
new_memory_mb = new_memory / (1024 * 1024)

print("\n===== SIMULASI PERUBAHAN =====")
print(f"Resolusi Baru         : {new_width} x {new_height}")
print(f"Bit Depth Baru        : {new_bit_depth} bit")
print(f"Ukuran Memori Baru    : {new_memory_mb:.2f} MB")

# ===============================
# 6. Representasi Matriks
# ===============================
print("\n===== REPRESENTASI MATRIKS (5x5 Piksel Pertama) =====")
print(img[:5, :5])

# ===============================
# 7. Representasi Vektor
# ===============================
vector = img.flatten()

print("\n===== REPRESENTASI VEKTOR =====")
print(f"Panjang Vektor        : {len(vector)} elemen")
print("10 nilai pertama vektor:")
print(vector[:10])

# ===============================
# 8. Analisis Intensitas
# ===============================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mean_intensity = np.mean(gray)
min_intensity = np.min(gray)
max_intensity = np.max(gray)

print("\n===== ANALISIS INTENSITAS =====")
print(f"Rata-rata Intensitas  : {mean_intensity:.2f}")
print(f"Intensitas Minimum    : {min_intensity}")
print(f"Intensitas Maksimum   : {max_intensity}")

if mean_intensity < 100:
    print("Kesimpulan: Citra cenderung gelap.")
else:
    print("Kesimpulan: Citra cukup terang.")

# ===============================
# 9. Manipulasi Dasar (Versi Variasi)
# ===============================

# Crop bagian atas (fokus langit & bulan)
crop = img[0:height//2, 0:width]

# Resize lebih kecil
resize = cv2.resize(img, (600, 400))

# Flip Horizontal
flip_horizontal = cv2.flip(img, 1)

# Flip Vertical
flip_vertical = cv2.flip(img, 0)

# ===============================
# 10. Menampilkan Semua Hasil (Satu per Satu)
# ===============================

def tampil_satu_satu(image, title):
    display_width = 500
    h, w = image.shape[:2]
    scale = display_width / w
    new_h = int(h * scale)
    img_small = cv2.resize(image, (display_width, new_h))

    cv2.imshow(title, img_small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

tampil_satu_satu(img, "Original")
tampil_satu_satu(crop, "Crop (Bagian Atas)")
tampil_satu_satu(resize, "Resize")
tampil_satu_satu(flip_horizontal, "Flip Horizontal")
tampil_satu_satu(flip_vertical, "Flip Vertical")