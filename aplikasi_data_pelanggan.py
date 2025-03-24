from tabulate import tabulate
from time import sleep
import re
data_pelanggan = [
    {
        "nama" : "Ari suseta",
        "alamat" : "DSN Plumbang Desa pandansari",
        "no_ip": "10.10.1.120",
        "no_hp" : "tidak ada"
    }
]

def tampilkan_menu():
    print("""
    Pilih menu berikut:
          1. Tambah data
          2. Edit data
          3. menampilkan data
          4. Cari data berdasarkan alamat Ip
          5. Delet data berdasarkan Ip
          6. exit
    """)

# function input data
def input_data(prompt, required=True, default=None, validate_ip=False, validate_phone=False):
    while True:
        value = input(prompt).strip()

        if required and not value:
            print("Input tidak boleh kosong")
            continue

        if not value and default is not None:
            return default
        
        if validate_ip:
            if not is_valid(value):
                print("Alamat Ip tidak valid!")
                continue

        if validate_phone:
            if not is_valid_phone(value):
                print("Nomor telepon tidak valid!")
                continue

        return value

# function validasi alamat ip
def is_valid(ip_addres):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(pattern, ip_addres):
        octets = ip_addres.split(".")
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    return False

# function cek ip duplikated
def ip_duplikated(data_pelanggan):
    while True:
        ip_address = input_data("Alamat Ip: ", validate_ip=True)
        if any(d["no_ip"] == ip_address for d in data_pelanggan):
            print("Alamat Ip sudah terdaftar, Masukan alamat Ip lain.")
        else:
            return ip_address

# function validasi no hp
def is_valid_phone(phone_number):
    pattern = r"^(0|\+62)[2-9][0-9]{8,11}$"
    return re.match(pattern, phone_number) is not None

# function tampil data
def tampil_data(data):
    for data in data_pelanggan:
        data_tabulate = [
            ["Nama", data["nama"]],
            ["Alamat", data["alamat"]],
            ["Ip Address", data["no_ip"]],
            ["No Hp", data["no_hp"]]
        ]
        print("\n"+ tabulate(data_tabulate, headers="firstrow", tablefmt="grid"))

# function edit data

def edit_data(data_pelanggan):
    # menampilkan data pelanggan
    tampil_data(data_pelanggan)
    while True:
        try:
            pilihan = int(input(f"Cari data yang mau di edit (1 - {len(data_pelanggan)})")) - 1
            data_edit = data_pelanggan[pilihan]
            break
        except (ValueError, IndexError) :
            print("Input tidak valid!")
    keys = ", ".join(data_edit.keys()) # mendapatkan key dari dictionary
    new_data = data_edit.copy() # membuat salinan data

    while True:
        key_edit = input(f"Masukan piliha yang mau di edit ({keys}): ").strip().lower()

        if key_edit in data_edit:
            if key_edit == 'no_ip':
                new_data[key_edit] = ip_duplikated(data_pelanggan)
            elif key_edit == 'no_hp':
                new_data[key_edit] = input_data("No Hp: ", validate_phone=True)
            else:
                new_data[key_edit] = input_data(f"{key_edit.capitalize()}: ")
            break
        else:
            print("Pilihan tidak valid!")
    data_pelanggan[pilihan] = new_data

# loop utama program
while True:
    tampilkan_menu()

    try:
        keyword = int(input("Masukan pilihan (1-6): ").strip())

        # cek jika pilihan diluar batas
        if keyword < 1 or keyword > 6:
            print("Pilihan tidak valid, Masukan angka antara 1-6")
            continue

        # tambah data
        if keyword == 1:
            print("=====Tambah Data=====")
            data = {}
            data["nama"] = input_data("Nama: ")
            data["alamat"] = input_data("Alamat: (opsional) ", required=False, default="tidak ada")
            # validasi ip unik
            data["no_ip"] = ip_duplikated(data_pelanggan)
            
            data["no_hp"] = input_data("No Hp: (opsional) ", required=False, default="tidak ada", validate_phone=True)

            data_pelanggan.append(data)
            
            print("Menambahkan data....")
            sleep(1)
            print("Data berhasil di tambahkan")
            sleep(1)

        # edit data
        if keyword == 2:
            edit_data(data_pelanggan)
            keyword = 3

        # menampilkan data
        if keyword == 3:
            tampil_data(data_pelanggan)

        # keluar dari program
        elif keyword == 6:
            print("Terimakasih! Program berhenti.")
            break

    except ValueError:
        print("Masukan angka yang benar")