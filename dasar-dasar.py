# print("Hallo World") mencetak kelayar

# variabel dan tipe data

# nama = "ari suseta" # string
# umur = 29 # integer
# tinggi = 168,8 # float
# belajar = True # boolean
#
# print(type(nama))
# print(type(umur))
# print(type(tinggi))
# print(type(belajar))

# mengambil input dari pengguna => selalu menghasilkan string

# nama = input("Masukan Nama anda: ")
# umur = input("Masukan umur anda: ")
#
# print(f"Nama: {nama}, Umur: {umur}")

# confersi tipe data

# angka1 = int(input("Masukan angka pertama: "))
# angka2 = int(input("Masukan angka kedua: "))

# print(f"Angka pertama: {angka1} \nangka kedua: {angka2}")

# hasil = angka1 + angka2
# print(f"Hasil dari penjumblahan {angka1} + {angka2} = {hasil}")


# operator(+, -, *, **, /, //, %)
# (tambah, kurang, kali, pangkat, bagi, pembagian bulat, modulus/sisa bagi)
#
# a = 10
# b = 3
#
# penjumblahan = a + b
# pengurangan = a - b
# perkalian = a * b
# pembagian = a / b
# modulus = a % b
# pangkat = a ** b
# bagi_bulat = a // b
#
# print(f"penjumblahan = {penjumblahan}")
# print(f"pengurngan = {pengurangan}")
# print(f"perkalian = {perkalian}")
# print(f"pembagian = {pembagian}")
# print(f"modulus = {modulus}")
# print(f"Pangkat = {pangkat}")
# print(f"bagi bulat = {bagi_bulat}")

"""
OPERATOR PERBANDINGAN

== (Sama dengan)	5 == 5	True
!= (Tidak sama dengan)	5 != 3	True
> (Lebih besar)	5 > 3	True
< (Lebih kecil)	5 < 3	False
>= (Lebih besar atau sama)	5 >= 5	True
<= (Lebih kecil atau sama)	3 <= 5	True
"""

# print(f"apakah a == b ({a == b})") # False
# print(f"apakah a != b ({a != b})") # True
# print(f"apakah a <= b ({a <= b})") # False

"""
OPERTOR LOGIKA

and	True and False	False
or	True or False	True
not	not True	False
"""

# STUDI KASUS KALKULATOR SEDERHANA

# print("Masukan angka")
# hasil = 0
#
# try:
#     a = float(input("angka pertama: "))
#     b = float(input("angka kedua: "))
#     print("Pilih opertor (+, -, *, /, %, **, //)")
#     operator = input("operator: ")
#
#     if operator == '+':
#         hasil = a + b
#     elif operator == '-':
#         hasil = a - b
#     elif operator == '*':
#         hasil = a * b
#     elif operator == "/":
#         if b == 0.0 :
#             print("tidak bisa di bagi 0")
#             exit()
#         hasil = a / b
#     elif operator == '%':
#         hasil = a % b
#     elif operator == '**':
#         hasil = a ** b
#     elif operator == '//':
#         if b == 0.0 :
#             print("tidak bisa di bagi 0")
#             exit()
#         hasil = a // b
#     else:
#         print("Operator tidak di kenali!")
#
#     print(f"Hasil = {hasil}")
# except ValueError:
#     print("Error : anda harus memasukan angka")


# percabangan

# umur = int(input("masukan umur anda: "))
#
# if umur >= 18:
#     print("Anda Sudah dewasa")
# elif umur >= 13:
#     print("Anda seorang remaja")
# else:
#     print("Anda masih anak anak")

"""
Buat program Python yang:

Meminta pengguna memasukkan sebuah angka.
Mengecek apakah angka tersebut positif, negatif, atau nol.
Menampilkan hasil yang sesuai.

"""
try:
    angka = int(input("Masukan Angka: "))

    if angka > 0 :
        print("Angka yang anda masukan positif")
    elif angka == 0:
        print("angka yang anda masukan nol")
    else:
        print("angka yang anda masukan negatif")
except ValueError:
    print("yang anda masukan bukan angka")