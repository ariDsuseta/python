import math
"""
📌 Apa Itu Function?
Function adalah blok kode yang dirancang untuk menjalankan tugas tertentu dan bisa digunakan kembali tanpa harus menulis ulang kodenya.

✨ Manfaat Menggunakan Function
✅ Menghindari pengulangan kode (reusability).
✅ Membuat program lebih terstruktur dan mudah dipahami.
✅ Mempermudah debugging.

"""
# membuat function
# def sapa() :
#     print("Halo, Selamat datang")

# menjalankan function
# sapa()

# function dengan parameter
# def sapa(nama):
#     print(f"Hallo, {nama} Selemat datang")

# nama = "Ari suseta"
# sapa(nama)
# sapa("Bagus")

# function dengan return

# def tambah(a,b):
#     return a+b
# a = 10
# b = 12
# hasil = tambah(a,b)
# print(f"Hasil Penjumblahan dari ({a} + {b}) = {hasil}")

# def luas_persegi_panjang(p,l):
#     return p * l

# p = 10
# l = 20

# hasil = luas_persegi_panjang(p,l)

# print(f"Hasil luas persegi panjang adalah {hasil}")

# rumus persegi panjang 2 * (p+l)

# def keliling_persegi_panjang(p, l):
#     return 2 * (p + l)

# p = 10
# l = 20
# hasil = keliling_persegi_panjang(p, l)
# print(f"Hasil dari Keliling persegi panjang adalah {hasil}")

# default parameter

# def sapa(nama = "Teman"):
#     print(f"Halo, {nama}!")

# sapa()
# sapa("Bagus")


# function dengan banyak parameter
# def info_buku(judul, penulis, tahun):
#     print(f"Judul: {judul}")
#     print(f"Penulis: {penulis}")
#     print(f"Tahun Terbit: {tahun}")

# info_buku("Laskar Pelangi", "Andrea Hirata", 2005)

"""function dengan parameter opsional
Python menyediakan *args untuk menerima banyak argumen tanpa batas dan **kwargs untuk menerima pasangan kunci-nilai.
*args => menyimpan nilai dalam bentuk tuple
**kwargs => menyimpan nilai dalam bentuk dictionary
"""


# def jumblahkan(*angka):
#     return sum(angka)

# hasil = jumblahkan(1,2,3,4,5,6)
# print(f"Hasil penjumblahan {hasil}")

# def biodata(**data):
#     for kunci, nilai in data.items():
#         print(f"{kunci} : {nilai}")

# biodata(nama="Budi", umur=25, kota="Jakarta")

"""
Latihan:
Buat function untuk menghitung volume balok dengan parameter p, l, dan t.

Function harus mengembalikan hasil perhitungan volume.

Panggil function dengan nilai p = 5, l = 3, t = 10.
"""

# def volume_balok(p,l,t):
#     return p * l * t

# p = 5
# l = 3
# t = 10

# hasil = volume_balok(p, l, t)
# print(f"Hasil dari Volume balok adalah {hasil}")

# Scope / lingkup variabel dalam function
# global variabel
# local variabel

# contoh global variabel

# x = 10

# def tampil_x():
#     print(x)

# tampil_x()

# contoh local variabel

# def tampil_x():
#     x = 10 # variabel lokal
#     print(x)

# tampil_x() # output 10
# print(x) # error

"""
3. Function Lambda (Anonymous Function)
Python punya function sederhana yang disebut lambda function.
Lambda function cocok untuk operasi yang singkat dan sekali pakai
"""

# contoh function biasa
# def kali(a,b):
#     return a * b
# print(kali(3,5))

# lambda function
# kali = lambda a,b : a * b
# print(kali(3,5))

"""
Latihan:
Buat function luas_lingkaran(r) untuk menghitung luas lingkaran.
    Gunakan return untuk mengembalikan hasil.
    Gunakan phi = 3.14.
Buat function sapa_pengguna(nama) yang mencetak sapaan tanpa return.
Buat lambda function untuk menghitung kuadrat dari sebuah angka.
"""

# def luas_lingkaran(r):
#     return 3.14 * r**2
# luas_lingkaran = lambda r : math.pi * r ** 2
# print(luas_lingkaran(5))

# sapa = lambda nama = "Teman": print(f"Hallo, {nama}!")
# sapa()
# sapa("Bastian")

# kuadrat = lambda a: a ** 2
# print(f"hasil dari kuadrat {kuadrat(3)}")

# hitung_diskon = lambda harga, diskon = 10 : harga - (harga * diskon / 100)

# harga_awal = 100000
# diskon_persen = 15
# # :,.0f → Agar angka memiliki format ribuan (contoh: Rp75,000).
# print(f"Harga Setelah diskon: Rp.{hitung_diskon(harga_awal, diskon_persen):,.0f}")

# hitung_diskon = lambda harga, diskon = 10 : max(0, harga - (harga * min(diskon, 100) / 100))

# harga_awal = 100000
# diskon_persen = 150
# # :,.0f → Agar angka memiliki format ribuan (contoh: Rp75,000).
# print(f"Harga Setelah diskon: Rp.{hitung_diskon(harga_awal, diskon_persen):,.0f}")

#  fungsi bawaan Python yang sering digunakan, seperti:
"""
map() → Menerapkan fungsi ke setiap elemen dalam iterable.

filter() → Menyaring elemen berdasarkan kondisi tertentu.

reduce() (dari functools) → Menggunakan fungsi untuk menggabungkan elemen secara berulang.

enumerate() → Memberi indeks pada elemen dalam iterable.
"""
# angka = [1,2,3,4,5]
# hasil = list(map(lambda x: x ** 2, angka))
# print(hasil)

# Gunakan map() untuk mengonversi list suhu dalam Celcius ke Fahrenheit dengan rumus:F=(C×9/5)+32

# suhu_celsius = [0, 10, 20, 30, 40]
# suhu_fahrenheit = list(map(lambda c : (c * 9/5) + 32, suhu_celsius))

# print(suhu_fahrenheit)

"""
filter(). Fungsi ini digunakan untuk menyaring elemen dalam iterable berdasarkan kondisi tertentu.
"""

# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# genap = list(filter(lambda x: x % 2 == 0, angka))
# print(genap)

# Gunakan filter() untuk menyaring suhu di bawah 25 derajat Celsius dari list berikut:
# suhu_celsius = [10, 15, 25, 30, 5, 40, 20]
# suhu_dingin = list(filter(lambda c : c < 25, suhu_celsius))
# print(suhu_dingin)

"""
🔹 Apa itu reduce()?
Fungsi reduce() digunakan untuk menerapkan suatu operasi pada seluruh elemen dalam list secara berulang hingga menghasilkan satu nilai akhir.
"""

# contoh menjumblahkan semua angka dalam list

# angka = [1, 2, 3, 4, 5]
# hasil = reduce(lambda x, y : x + y, angka)

# print(hasil)
# from functools import reduce
# angka = [2, 3, 4, 5]
# hasil_kali = reduce(lambda x, y: x * y, angka)
# print(hasil_kali)

"""
🔹 Apa itu enumerate()?
enumerate() digunakan saat kita ingin mengakses indeks dan nilai dari suatu iterable dalam perulangan.
"""
# angka = [10, 20, 30, 40, 50]

# for i, x in enumerate(angka, start=1):
#     print(f"{i}. {x}")

"""
🔹 Studi Kasus: Mencari Index dari Elemen Tertentu
Misalkan kita punya daftar nama berikut:

nama_siswa = ["Budi", "Siti", "Andi", "Dewi", "Rudi"]
Tugas kamu adalah mencari index dari "Andi" dengan enumerate() dan mencetaknya seperti ini:

"Andi" ada di index ke-2
📌 Petunjuk: Gunakan if di dalam for loop!
"""

# nama_siswa = ["Budi", "Siti", "Andi", "Dewi", "Rudi"]
# siswa_dicari = "rudi"

# for i, nama in enumerate(nama_siswa):
#     if(nama.strip().lower() == siswa_dicari.strip().lower()):
#         print(f"{siswa_dicari} ada di index ke-{i}")


"""
🔹 Studi Kasus: Menandai Elemen yang Sesuai
Kita punya daftar skor ujian siswa:

skor_siswa = [85, 60, 90, 40, 75]
Tugas kamu:

Gunakan enumerate() untuk menampilkan skor beserta nomor urutnya.

Tandai skor yang di bawah 70 dengan teks "Perlu perbaikan!" seperti ini:

1. 85
2. 60 - Perlu perbaikan!
3. 90
4. 40 - Perlu perbaikan!
5. 75
📌 Petunjuk: Gunakan if di dalam loop!
"""

skor_siswa = [85, 60, 90, 40, 75]
nilai_standart = 70

# for i, nilai in enumerate(skor_siswa, start=1):
#     if nilai < nilai_standart:
#         print(f"{i}. {nilai} - Perlu perbaikan!")
#     else :
#         print(f"{i}. {nilai}")

# menambahkan status
# for i, nilai in enumerate(skor_siswa, start=1):
#     if nilai < nilai_standart:
#         status = "Perlu perbaikan!"
#     else:
#         status = "Lulus"
    
#     print(f"{i}. {nilai} - {status}")

"""
Studi Kasus: Mengelompokkan Angka Genap dan Ganjil
Kita akan membuat program yang dapat memisahkan angka genap dan ganjil dari sebuah daftar angka.

Tugasmu:

Buatlah daftar angka dari 1 hingga 20.

Gunakan filter() untuk memisahkan angka genap dan angka ganjil.

Cetak hasilnya dalam format berikut:

Angka Genap: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Angka Ganjil: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# angka_genap = list(filter(lambda x : x % 2 == 0, angka))
# angka_ganjil = list(filter(lambda x : x % 2 == 1, angka))

# print(f"Angka Genap = {angka_genap}")
# print(f"Angka Ganjil = {angka_ganjil}")



"""
Tantangan Baru: Mengelompokkan Angka ke dalam Kelipatan
Buat program untuk mengelompokkan angka dari 1 hingga 50 ke dalam:

Kelipatan 3
Kelipatan 5
Kelipatan 3 dan 5
"""
# angka = list(range(1,51))

# kelipatan3 = list(filter(lambda a : a % 3 == 0, angka))
# kelipatan5 = list(filter(lambda a : a % 5 == 0, angka))
# # kelipatan3_kelipatan5 = list(filter(lambda a: a % 3 == 0 and a % 5 == 0, angka))
# kelipatan3_kelipatan5 = list(set(kelipatan3) & set(kelipatan5))

# print(kelipatan3)
# print(kelipatan5)
# print(kelipatan3_kelipatan5)

# Coba ubah program ini agar bisa menerima input angka dari pengguna! 🔥
while True:
    try:
        angka_user = int(input("Masukan angka: "))

        # jika angka dibawah 10
        if angka_user < 10:
            print("Masukan angka setidaknya lebih besar dari 10")
            continue

        angka = list(range(1, angka_user + 1))
        kelipatan3 = list(filter(lambda a : a % 3 == 0, angka))
        kelipatan5 = list(filter(lambda a : a % 5 == 0, angka))
        kelipatan_keduanya = list(set(kelipatan3) & set(kelipatan5))

        print(f"Kelipatan 3 = {kelipatan3}")
        print(f"Kelipatan 5 = {kelipatan5}")
        print(f"Kelipatan 3 dan kelipatan 5 = {kelipatan_keduanya}")
        break
        
    except ValueError:
        print("Masukan angka yang benar!")