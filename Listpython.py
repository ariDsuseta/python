# list adalah kumpulan nilai yang dapat di ubah dan di akses berdasarkan indeksnya

# angka = [1,3,2,4,5,63,42,32]
# nama = ["Ari suseta", "Bastian", "Eko", "Prass"]
#
# print(angka)
# print(nama[0])
#
# # operasi pada list
#
# print("=========================================")
# print(f"sebelum = {angka}")
# angka.append(90) #menambahkan element di akhir
# print(f"menambahkan = {angka}")
# angka.remove(4) # Menghapus elemen 4
# print(f"menghapus = {angka}")
# angka.insert(4,100) # menyisipakn elemen berdasarkan indeksnya
# print(f"insert = {angka}")
# angka.sort() # mengurutkan nilai
# print(f"sort = {angka}")
# print("=========================================")
#
# # tuple = tidak bisa di ubah maupun di hapus dan lebih cepat dari list
# data = (1,2,3)
# print(data[1])
#
# konversi_list_tupel = tuple(angka)
# print(konversi_list_tupel)


"""

Studi Kasus
Tantangan:
Minta pengguna memasukkan 5 angka bulat dan simpan dalam List.
Tampilkan angka-angka tersebut dalam urutan terbalik.
Konversi List ke Tuple dan tampilkan hasilnya.

"""

# try :
#     # print("Masukan angka bulat")
#     # angka1 = int(input("Angka pertam: "))
#     # angka2 = int(input("Angka kedua: "))
#     # angka3 = int(input("Angka ketiga: "))
#     # angka4 = int(input("Angka keempat: "))
#     # angka5 = int(input("Angka kelima: "))
#     # hasil = [angka5, angka4, angka3, angka2, angka1]
#     #
#     # hasil_tuple = tuple(hasil)
#     # print(hasil_tuple)
#
#     angka = []
#     for x in range(5):
#         angka.append(int(input(f"Masukan angka ke {x + 1} :")))
#
#     angka.reverse()
#     hasil_tuple = tuple(angka)
#
#     print(hasil_tuple)
#
# except ValueError:
#     print("Mohon masukan angka!")



# studi kasus 1
"""
Studi Kasus 1: Mencari Nilai Maksimum & Minimum
Tantangan:

Minta pengguna memasukkan 5 angka bulat dan simpan dalam List.
Tampilkan angka dalam urutan asli.
Tampilkan angka terbesar & terkecil dari List.
Konversi List ke Tuple dan tampilkan hasilnya.

"""

# try:
#     angka = []
#
#     for x in range(5):
#         angka.append(int(input(f"Masukan angka ke-{x+1}: ")))
#
#     print("\nAngka yang dimasukkan:",angka)
#     print("Angka dalam urutan terkecil:", sorted(angka))
#     print(f"Angka terbesar adalah {max(angka)} dan angka terkecil adalah {min(angka)}")
#
#     angka_tuple = tuple(angka)
#     print("Hasil dalam bentuk tuple:", angka_tuple)
#
# except ValueError:
#     print("Mohon masukan angka yang valid")

# STUDI KASUS 2

"""

Studi Kasus 2: Menghitung Rata-rata
(jumblah semua data : banyaknya data)
Tantangan:

Minta pengguna memasukkan jumlah angka yang diinginkan.
Simpan angka dalam List.
Hitung dan tampilkan rata-rata dari semua angka.
Konversi List ke Tuple & tampilkan hasilnya.
💡 Hint: Gunakan sum() dan len().

"""

# try:
#     angka = int(input("Masukan jumblah angka: "))
#
#     if angka < 1:
#         print("Jumlah angka harus lebih dari 0!")
#     else :
#         nilai = []
#         for a in range(angka):
#             nilai.append(float(input(f"Masukan nilai ke-{a+1}: ")))
#
#         rata_rata = sum(nilai) / len(nilai)
#         nilai_tuple = tuple(nilai)
#
#         print("\nData nilai: ",nilai)
#         print(f"Rata-rata nilai: {rata_rata:.2f}")
#         print(f"Hasil dari bentuk tuple: {nilai_tuple}")
#
# except ValueError:
#     print("Mohon masukan angka yang Valid!")


# STUDI KASUS 3

"""
Studi Kasus 3: Menemukan Angka yang Dicari
Tantangan:

Minta pengguna memasukkan beberapa angka dan simpan dalam List.
Minta pengguna memasukkan angka yang ingin dicari.
Jika angka ada dalam List, tampilkan indeksnya.
Jika tidak ditemukan, beri pesan "Angka tidak ditemukan".
💡 Hint: Gunakan .index() atau cek dengan if angka in list.
"""


# try:
#     angka_input = input("Masukan angka-angka yang di pisahkan dengan koma: ")
#     if angka_input.endswith(','):
#         angka_input = angka_input[:-1]

#     angka_string = angka_input.split(',')

#     angka_list = [int(angka.strip()) for angka in angka_string]
#     angka_cari = int(input("Masukan angka yang ingin anda cari: "))

#     try:
#         angka_index = angka_list.index(angka_cari)
#         print(f"angka {angka_cari} mempunyai index ({angka_index})")
#     except ValueError:
#         print("Angka yang anda cari tidak di temukan")

# except ValueError:
#     print("Mohon masukan angka yang Valid")

try:
    angka_input = input("Masukkan angka-angka yang dipisahkan dengan koma: ").strip()

    # Cek apakah input kosong atau hanya koma
    if not angka_input or angka_input.replace(',', '').strip() == '':
        print("Mohon masukkan minimal satu angka yang valid!")
    else:
        # Menghapus koma di akhir jika ada
        if angka_input.endswith(','):
            angka_input = angka_input[:-1]

        angka_string = angka_input.split(',')

        # Konversi string ke integer, sambil menghapus spasi
        angka_list = [int(angka.strip()) for angka in angka_string]

        angka_cari = int(input("Masukkan angka yang ingin Anda cari: "))

        # Cek apakah angka ada dalam list
        indeks_list = [i for i, num in enumerate(angka_list) if num == angka_cari]

        if indeks_list:
            print(f"Angka {angka_cari} ditemukan pada indeks: {', '.join(map(str, indeks_list))}")
        else:
            print(f"Angka {angka_cari} tidak ditemukan dalam list.")

except ValueError:
    print("Mohon masukkan angka yang valid!")
