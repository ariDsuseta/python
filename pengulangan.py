# pengulangan for

# for x in range(1,6):
#     print(f"For ke {x}")
#
# counter = 1
# while counter <= 5:
#     print(f"While ke {counter}")
#     counter += 1

"""
Buat program Python yang:

Meminta pengguna memasukkan bilangan bulat positif.
Menampilkan deret faktor dari bilangan tersebut (bilangan yang bisa membagi habis angka tersebut).
"""

# try:
#     bilangan = int(input("Masukan bilangan bulat positif: "))
#     hasil = 1
#     if bilangan <= 0:
#         print("Mohon masukan bilangan bulat positif")
#     else:
#         print(bilangan, '! = ', sep='', end='')
#         for x in range(1, bilangan+1):
#             hasil = hasil * x
#             print(x, end=' ')
#             if bilangan != x :
#                 print("*", end=' ')
#         print(f"= {hasil}")
# except ValueError:
#     print("Yang anda masukan bukan bilangan bulat / tidak di ketahui")

"""
Studi Kasus Baru:
Buat program Python yang:

Meminta pengguna memasukkan bilangan bulat positif.
Menampilkan semua faktor dari bilangan tersebut (bilangan yang bisa membagi habis angka itu).

TIPS

1. Pahami Konsep Faktor
Faktor dari suatu bilangan adalah angka yang bisa membagi habis bilangan tersebut (tanpa sisa).
Contoh: 12 memiliki faktor: 1, 2, 3, 4, 6, 12 karena semua angka ini dapat membagi 12 tanpa sisa.
2. Gunakan Perulangan
Cek setiap angka dari 1 hingga bilangan apakah bisa membagi habis bilangan tersebut.
Gunakan operator modulus % untuk mengecek sisa bagi (x % y == 0).
3. Gunakan List untuk Menyimpan Faktor
Bisa pakai list.append() untuk menyimpan semua faktor.
Terakhir, tampilkan hasilnya dengan format yang rapi.

"""
try:
    while True :
        angka = int(input("Masukan bilangan bulat positif: "))
        if angka < 1:
            print("yang anda masukan bukan bilangan bulat positif")
            continue
        break

    print(f"Faktor dari {angka} adalah", end=' ')
    for x in range(1, angka+1):
        if angka % x == 0:
            # if x == angka:
            #     print(angka, end='')
            #     break
            print(x, end=', ')
    print("\b\b")
except ValueError:
    print("Yang anda masukan bukan angka")

