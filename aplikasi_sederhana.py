# ke satu

# while True:
#     try:
#         angka_user = int(input("Masukan batas angka: "))
#
#         if angka_user < 10:
#             print("masukan angka setidaknya lebih besar dari 10")
#             continue
#
#         kelipatan = int(input("Masukan kelipatan: "))
#
#         hasil = [x for x in range(1, angka_user + 1) if x % kelipatan == 0]
#
#         print(f"Kelipatan {kelipatan} hingga {angka_user}: {hasil}")
#         break
#     except ValueError:
#         print("Masukan angka yang benar!")

# versi ke dua

# while True:
#     try:
#         angka_user = int(input("Masukan batas angka: "))
#
#         if angka_user < 10:
#             print("Masukan angka setidaknya lebih beas dari 10")
#             continue
#
#         kelipatan1 = int(input("Masukan kelipata pertama: "))
#         kelipatan2 = int(input("Masukan kelipatan ke dua: "))
#
#         angka = list(range(1, angka_user + 1))
#         hasil1 = [x for x in angka if x % kelipatan1 == 0]
#         hasil2 = [x for x in angka if x % kelipatan2 == 0]
#         hasil_keduanya = list(set(hasil1) & set(hasil2))
#
#         print("\n1. Tampilkan hanya kelipatan pertama")
#         print("2. Tampilkan hanya kelipatan kedua")
#         print("3. Tampilkan kelipatan pertama dan kedua")
#         print("4. Tampilkan kelipatan yang merupakan kedua-duanya")
#
#         pilihan = input("Pilih opsi (1/2/3/4): ")
#
#         if pilihan == '1':
#             print(f"Kelipatan {kelipatan1}: {hasil1}")
#         elif pilihan == '2':
#             print(f"Kelipatan {kelipatan2}: {hasil2}")
#         elif pilihan == '3':
#             print(f"Kelipatan {kelipatan1}: {hasil1}")
#             print(f"Kelipatan {kelipatan2}: {hasil2}")
#         elif pilihan == '4':
#             print(f"Kelipatan {kelipatan1} dan {kelipatan2}: {hasil_keduanya}")
#         else:
#             print("Pilihan tidak valid")
#
#         break
#     except ValueError:
#         print("Masukan angka yang benar!")


# versi ke tiga
from tabulate import tabulate
while True:
    try:
        angka_user = int(input("Masukan batas angka: "))

        if angka_user < 10:
            print("Masukan angka setidaknya lebih beas dari 10")
            continue

        kelipatan1 = int(input("Masukan kelipata pertama: "))
        kelipatan2 = int(input("Masukan kelipatan ke dua: "))

        angka = list(range(1, angka_user + 1))
        hasil1 = [x for x in angka if x % kelipatan1 == 0]
        hasil2 = [x for x in angka if x % kelipatan2 == 0]
        hasil_keduanya = list(set(hasil1) & set(hasil2))

        data = [
            ["Kelipatan", kelipatan1, kelipatan2, f"{kelipatan1} & {kelipatan2}"],
            ["Hasil", hasil1, hasil2, hasil_keduanya]
        ]

        print("\n" + tabulate(data, headers="firstrow", tablefmt="grid"))


        break
    except ValueError:
        print("Masukan angka yang benar!")
