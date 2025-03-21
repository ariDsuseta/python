"""
Dictionary adalah struktur data yang menyimpan data dalam format key-value pair.
👉 Mirip dengan kamus, di mana kata adalah key, dan artinya adalah value.
"""

# sintaks dasar dictionary
# data_mahasiswa = {
#     "nama" : "Bagus",
#     "umur" : 21,
#     "jurusan" : "Informatika"
# }

# print(data_mahasiswa["nama"])
# print(data_mahasiswa["umur"])
# print(data_mahasiswa["jurusan"])

"""
Operasi Dasar pada Dictionary
__________________________________________________________________
Operasi	                |       Contoh	         |         Hasil
------------------------------------------------------------------
Menambahkan data        |   dict["key"] = value  |  dict["alamat"] = "Jakarta"
Mengubah data           |	dict["umur"] = 22    |  Umur jadi 22
Menghapus data          |   del dict["jurusan"]  |	Hapus "jurusan"
Mengecek key            |   "nama" in dict       |	True jika ada
Mendapatkan semua key	|   dict.keys()          |	dict_keys([...])
Mendapatkan semua value |	dict.values()	     |  dict_values([...])
"""

# data_mahasiswa = {
#     "nama" : "Bagus",
#     "umur" : 21,
#     "jurusan" : "Informatika"
# }
# data_mahasiswa["alamat"] = "jakarta"
# data_mahasiswa["umur"] = 22
# del data_mahasiswa["alamat"]
# cek_key = "nama" in data_mahasiswa
# key_all = data_mahasiswa.keys()
# values_all = data_mahasiswa.values()

# print(data_mahasiswa)
# print(cek_key)
# print(key_all)
# print(values_all)

"""
📌 Studi Kasus Dictionary
Buatlah program input data siswa!

Program meminta nama, usia, dan kelas siswa.
Simpan dalam Dictionary.
Cetak hasilnya dalam format yang rapi.
"""

# print("Isikan data berikut ini")
# try:
#     while True:
#         data_mahasiswa = {}
#         daftar_jurusan = ["Informatika", "Industri", "Mesin"]
#         nama = input("Nama: ")
#         umur = int(input("Umur: "))
#         jurusan = input("Jurusan: ")
#         # cek apakah input kosong
#         if(nama.strip() == "" or jurusan.strip() == ""):
#             print("mohon masukan data yang valid")
#             continue
#         else:
#             # cek jika nama kurang dari 5 karakter
#             if(len(nama) <= 5):
#                 print("Data nama minimal 5 karakter")
#                 continue
#             else:
#                 data_mahasiswa["nama"] = nama

#             # cek jika jurusan tidak ada dalam daftar dan konvert lowercase
#             if jurusan.lower() in [x.lower() for x in daftar_jurusan]:
#                 data_mahasiswa["jurusan"] = jurusan
#             else:
#                 print("Data jurusan tidak terdaftar!")
#                 continue
            
#             data_mahasiswa['umur'] = umur
#         cek_data = input("cek kelengkapan data anda tekan (y) jika data udah lengkap dan tekan (n) jika belum lengkap: ")
#         if(cek_data.lower() == 'n'): continue
#         print("\nData anda sudah terdaftar")
#         print("===============================")
#         print(f"\nNama: {data_mahasiswa['nama']} \nUmur: {data_mahasiswa['umur']} \nJurusan: {data_mahasiswa['jurusan']}")
#         print("===============================")
#         break
# except ValueError:
#     print("Masukan data umur yang valid!")

# print("=== Isikan Data Mahasiswa ===")
# try:
#     data_mahasiswa = {}
#     daftar_jurusan = ["Informatika", "Industri", "Mesin"]

#     while True:
#         nama = input("Nama: ").strip()
#         if len(nama) < 5:
#             print("❌ Nama minimal 5 karakter!")
#             continue
#         data_mahasiswa["nama"] = nama.title()  # Format nama jadi lebih rapi

#         try:
#             umur = int(input("Umur: "))
#             if umur <= 0:
#                 print("❌ Umur harus lebih dari 0!")
#                 continue
#         except ValueError:
#             print("❌ Masukkan angka yang valid untuk umur!")
#             continue
#         data_mahasiswa["umur"] = umur

#         jurusan = input("Jurusan: ").strip()
#         if jurusan.lower() in [x.lower() for x in daftar_jurusan]:
#             data_mahasiswa["jurusan"] = jurusan.title()
#         else:
#             print("❌ Data jurusan tidak terdaftar! Pilihan: Informatika, Industri, Mesin")
#             continue

#         cek_data = input("Cek kelengkapan data anda (y/n): ").strip().lower()
#         if cek_data == 'y':
#             break  # Keluar dari loop jika data sudah benar
#         print("Silakan masukkan kembali data Anda.")

#     # Menampilkan data dengan tampilan yang lebih rapi
#     print("\n✅ Data Anda Telah Terdaftar ✅")
#     print("===============================")
#     print(f"Nama    : {data_mahasiswa['nama']}")
#     print(f"Umur    : {data_mahasiswa['umur']} tahun")
#     print(f"Jurusan : {data_mahasiswa['jurusan']}")
#     print("===============================")

# except Exception as e:
#     print(f"Terjadi kesalahan: {e}")

"""
ChatGPT bilang:
📌 Studi Kasus Baru - Dictionary
Buatlah program sederhana untuk mengelola data buku dalam perpustakaan menggunakan dictionary. Program harus memiliki fitur berikut:

1️⃣ Menambahkan buku (Judul, Penulis, Tahun Terbit)
2️⃣ Menampilkan daftar buku yang telah dimasukkan
3️⃣ Mencari buku berdasarkan judul
4️⃣ Menghapus buku berdasarkan judul
5️⃣ Keluar dari program

⚠ Catatan:

Gunakan dictionary untuk menyimpan data buku.
Pastikan judul buku unik, tidak boleh ada duplikasi.
Format tampilan output harus rapi dan mudah dibaca.
Gunakan perulangan dan validasi input agar program lebih kuat.
"""

print("=====Data buku perpustakaan=====")
try:
    data_buku = [
        {
        "judul": "Laskar Pelangi",
        "penulis": "Andrea Hirata",
        "tahun_terbit": 2005,
    },
    {
        "judul": "Bumi Manusia",
        "penulis": "Pramoedya Ananta Toer",
        "tahun_terbit": 1980,
    },
    {
        "judul": "Filosofi Teras",
        "penulis": "Henry Manampiring",
        "tahun_terbit": 2018,
    },
    {
        "judul": "Sapiens: Riwayat Singkat Umat Manusia",
        "penulis": "Yuval Noah Harari",
        "tahun_terbit": 2011,
    },
    {
        "judul": "Negeri 5 Menara",
        "penulis": "Ahmad Fuadi",
        "tahun_terbit": 2009,
    }
    ]
    print("Masukan keywoard berikut ini")
    print("""
    1. menambah data buku
    2. menampilkan daftar buku
    3. mencari buku berdasarkan judul
    4. menghapus buku berdasarkan judul
    5. Memperbarui informasi buku berdasarkan judul
    6. Menampilkan jumlah total buku
    7. exit
          
    !!! masukan pilihan menggunakan angka !!!
""")
    while True:
        keyword = 0
        jml_keywoard = 7
        data = {}
        try:
            keyword = int(input("Keywoard: "))
            # cek jika key word < 1
            if keyword < 1 or keyword > jml_keywoard:
                print("keyword tidak boleh lebih kecil 0 dan tidak boleh lebih besar dari 5")
                continue
        except ValueError:
            print("Masukan keywoard yang valid!")
            continue
        
        if keyword == 1:
            # 1️⃣ Menambahkan buku (Judul, Penulis, Tahun Terbit)
            # judul
            while True:
                judul = input("Judul buku: ").strip()

                if len(judul) < 5:
                    print("❌ Judul minimal 5 karakter!")
                    continue
                data["judul"] = judul
                break
            
            # penulis
            while True:
                penulis = input("Penulis: ").strip()

                if len(penulis) < 5:
                    print("❌ Nama penulis minimal 5 karakter!")
                    continue
                data['penulis'] = penulis
                break
            
            # tahun terbit
            while True:
                try:
                    tahun_terbit = int(input("tahun terbit: ").strip())
                    if tahun_terbit <= 0:
                        print("tahun harus lebih dari 0")
                        continue

                except ValueError:
                    print("Masukan tahun yang valid")
                    continue

                data["tahun_terbit"] = tahun_terbit
                break
            data_buku.append(data)

        # 2️⃣ Menampilkan daftar buku yang telah dimasukkan
        if keyword == 2:
            for i, databook in enumerate(data_buku):
                print(f"======== buku ke {i+1} ==========")
                print(f"Judul Buku: {databook["judul"]}")
                print(f"Penulis: {databook["penulis"]}")
                print(f"Tahun terbit: {databook["tahun_terbit"]}")
                print("=============================")
        # 3️⃣ Mencari buku berdasarkan judul
        if keyword == 3:
            while True:
                cari = input("Search buku: ").strip().lower()
                cari_buku = [buku for buku in data_buku if buku["judul"].strip().lower() == cari]
                if len(cari_buku) == 0:
                    print("Buku tidak di temukan!")
                    continue
                
                print("=============================")
                print(f"Judul Buku: {cari_buku[0]["judul"]}")
                print(f"Penulis: {cari_buku[0]["penulis"]}")
                print(f"Tahun terbit: {cari_buku[0]["tahun_terbit"]}")
                print("=============================")
                break
        # 4️⃣ Menghapus buku berdasarkan judul
        if keyword == 4:
            while True:
                print("\nDelet buku berdasarkan judul")
                cari = input("judul: ").strip().lower()
                ex = False
                for i, buku in enumerate(data_buku):
                    if buku["judul"].strip().lower() == cari :
                        data_buku.pop(i)
                        print("Data berhasil di hapus!")
                        ex = True
                if ex: break
                # jika tidak ketemu
                print("Buku tidak di temukan")
                continue
        # 5️⃣ Memperbarui informasi buku berdasarkan judul
        if keyword == 5 :
            print("Dalam Pembaruan")
        # 6️⃣ Menampilkan jumlah total buku
        if keyword == 6 :
            print(f"Total jumblah buku: {len(data_buku)}")

        # 7️⃣Keluar dari program
        if keyword == 7 : break
    
except Exception as e:
    print(f"Terjadi Kesalah: {e}")