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

# function validasi no hp
def is_valid_phone(phone_number):
    pattern = r"^(0|\+62)[2-9][0-9]{8,11}$"
    return re.match(pattern, phone_number) is not None

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
            while True:
                ip_address = input_data("Alamat Ip: ", validate_ip=True)
                if any(d["no_ip"] == ip_address for d in data_pelanggan):
                    print("Alamat Ip sudah terdaftar, Masukan alamat Ip lain.")
                else:
                    data["no_ip"] = ip_address
                    break
            
            data["no_hp"] = input_data("No Hp: (opsional) ", required=False, default="tidak ada", validate_phone=True)

            data_pelanggan.append(data)
            break

        # keluar dari program
        elif keyword == 6:
            print("Terimakasih! Program berhenti.")
            break

    except ValueError:
        print("PMasukan angka yang benar")