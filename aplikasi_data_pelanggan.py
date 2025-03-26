from tabulate import tabulate
from time import sleep
import re
data_pelanggan = [
    {
        "nama" : "Bagus",
        "alamat" : "DSN Contoh Desa Sembarang",
        "no_ip": "10.10.1.120",
        "no_hp" : "tidak ada"
    },
    {
        "nama" : "Prass",
        "alamat" : "DSN Contoh Desa Kupu",
        "no_ip": "10.10.1.12",
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
def tampil_data(data_pelanggan, id=False, prompt=None):
    if prompt is not None:
        sleep(1)
        print(prompt)
        sleep(0.5)

    for i, data in enumerate(data_pelanggan):
        if id:
            data_tabulate = [
                ["ID", i],
                ["Nama", data["nama"]],
                ["Alamat", data["alamat"]],
                ["Ip Address", data["no_ip"]],
                ["No Hp", data["no_hp"]]
            ]
        else:
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
            pilihan = int(input(f"Cari data yang mau di edit (1 - {len(data_pelanggan)}) ")) - 1
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

# fungction pecarian data
def cari_pelanggan_ip_rgx(prompt, data_pelanggan):
    while True:
        cari = input(prompt)
        hasil = [p for p in data_pelanggan if re.search(rf"\b{re.escape(cari)}\b", p["no_ip"])]
        if hasil:
            return hasil
        
        print("Data tidak di temukan!")
    
# function delet data
def delete_data_pelanggan(prompt, data_pel):
    while True:
        cari = input(prompt).strip()
        hasil_pencarian = [p for p in data_pel if re.search(rf"\b{re.escape(cari)}\b", p["no_ip"])]

        if hasil_pencarian:
            break

        print("Data tidak di temukan!")

    # tampilkan hasil dan kasih id nya
    tampil_data(hasil_pencarian, id=True, prompt="\nHasil Pencarian data!")

    # memilih data yang akan di hapus
    while True:
        if len(hasil_pencarian) == 1:
            id_hapus = 0
        else:
            id_hapus = input("Masukan id data yang mau dihapus: ").strip()
            if id_hapus.isdigit() and 0 <= int(id_hapus) < len(hasil_pencarian):
                id_hapus = int(id_hapus)
            else:
                print("ID tidak valid! Silakan coba lagi.")
                continue

        konfirmasi = input("Apakah anda yakin ingin menghapus data ini? (y/n) : ").strip().lower()
        if konfirmasi in ["y", ""]:
            break
        else:
            print("Penghapusan di batalkan.")
            return
    
    # menghapus data berdasarkan index dari "Hasil pencarian"
    id_data_hapus = next(i for i, data in enumerate(data_pel) if data == hasil_pencarian[id_hapus])
    del data_pel[id_data_hapus]
    
    print("Manghapus data", end=" ", flush=True)
    for x in range(1, 6):
        print(">", end="", flush=True)
        sleep(0.5)
        if x == 5: print(">")
    sleep(1)
    print("Data berhasil di hapus!")

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

        # pencarian data
        if keyword == 4:
            
            hasil_pencarian = cari_pelanggan_ip_rgx("Masukan keyword Ip (.20 / 20 / 1.20 / lengkap): ", data_pelanggan)
            tampil_data(hasil_pencarian)

        # delete data
        if keyword == 5:
            delete_data_pelanggan("Masukan keyword Ip (.20 / 20 / 1.20 / lengkap): ", data_pelanggan)

        # keluar dari program
        elif keyword == 6:
            print("Terimakasih! Program berhenti.")
            break

    except ValueError:
        print("Masukan angka yang benar")