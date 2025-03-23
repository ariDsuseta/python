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

hitung_diskon = lambda harga, diskon = 10 : max(0, harga - (harga * min(diskon, 100) / 100))

harga_awal = 100000
diskon_persen = 150
# :,.0f → Agar angka memiliki format ribuan (contoh: Rp75,000).
print(f"Harga Setelah diskon: Rp.{hitung_diskon(harga_awal, diskon_persen):,.0f}")