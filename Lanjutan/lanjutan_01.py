# Exception Handling
# try:
#     angka = int(input("Masukan angka: "))
#     hasil = 10 / angka
#     print(f"Hasil = {hasil}")
# except ZeroDivisionError:
#     print("Tidak bisa membagi dengan nol!")
# except ValueError:
#     print("Input Harus berupa angka!")

# Menangani Banyak Jenis Error dalam Satu Blok

# try:
#     angka = int(input("Masukan angka: "))
#     hasil = 10 / angka
#     print(f"Hasil = {hasil}")
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Terjadi kesalahan: {e}")

# else dalam Exception Handling

# try:
#     angka = int(input("Masukan angka: "))
#     hasil = 10 / angka
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Terjadi kesalahan: {e}")
# else:
#     print(f"Hasil = {hasil}") # akan di jalankan jika tidak ada error

# def animasi(prompt, angka, sl= 0.5):
#     print(prompt, end="", flush=True)
#     for i in range(1, angka+1):
#         sleep(sl)
#         print(".", end="", flush=True)
#
#     print("")
#
# # finally untuk Eksekusi Tetap Dilakukan
# from time import sleep
# try:
#     file = open("data.txt", "r")
#     animasi("Membuka File ", 5)
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("File tidak di temukan")
# finally:
#     animasi("Menutup file ", 5)
#     file.close()

# Membuat Exception Sendiri dengan raise

# def cek_usia(umur):
#     if umur < 18:
#         raise ValueError("Usia minimal harus 18 tahun!")
#     return "Akses diberikan"
#
# try:
#     usia = int(input("Masukan usia anda: "))
#     print(cek_usia(usia))
# except ValueError as e:
#     print(f"Error: {e}")


"""
Latihan

Buat program yang:

Meminta user memasukkan dua angka.

    1. Membagi angka pertama dengan angka kedua.

    2. Tangani ZeroDivisionError dan ValueError dengan pesan khusus.

    3. Gunakan else untuk mencetak hasil jika tidak ada error.

    4. Gunakan finally untuk mencetak "Program selesai.".

"""

def checked_num_bagi(angka1, angka2):
    # if angka1.isdigit() and angka2.isdigit():
    #
    #     if int(angka2) == 0:
    #         raise ZeroDivisionError("Anda tidak boleh Membagi dengan nol!")
    #
    #     return int(angka1) / int(angka2)
    #
    # else:
    #     raise ValueError("Masukan angka yang benar!")
    try:
        angka1 = int(angka1)
        angka2 = int(angka2)

        if angka2 == 0:
            raise ZeroDivisionError("Anda tidak boleh membagi dengan nol!")

        return angka1 / angka2
    
    except ValueError:
        raise ValueError("Masukan angka yang benar!")

try:
    angka1 = input("Masukan angka pertama: ")
    angka2 = input("Masukan angka kedua: ")
    hasil = checked_num_bagi(angka1, angka2)

except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")

else:
    print(f"Hasil = {hasil}")

finally:
    print("Program selesai.")