print("===== Data Buku Perpustakaan =====")
try:
    # Data buku awal
    data_buku = [
        {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun_terbit": 2005},
        {"judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun_terbit": 1980},
        {"judul": "Filosofi Teras", "penulis": "Henry Manampiring", "tahun_terbit": 2018},
        {"judul": "Sapiens: Riwayat Singkat Umat Manusia", "penulis": "Yuval Noah Harari", "tahun_terbit": 2011},
        {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun_terbit": 2009}
    ]

    # Fungsi untuk menampilkan menu utama
    def tampilkan_menu():
        print("""
        Pilih menu berikut:
        1. Menambah data buku
        2. Menampilkan daftar buku
        3. Mencari buku berdasarkan judul
        4. Menghapus buku berdasarkan judul
        5. Memperbarui informasi buku berdasarkan judul
        6. Menampilkan jumlah total buku
        7. Keluar
        """)

    while True:
        tampilkan_menu()
        try:
            keyword = int(input("Masukkan pilihan (1-7): "))
            if keyword < 1 or keyword > 7:
                print("Pilihan tidak valid, masukkan angka antara 1-7.")
                continue
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        # Menambahkan buku baru
        if keyword == 1:
            data = {}
            data["judul"] = input("Judul buku: ").strip()
            data["penulis"] = input("Penulis: ").strip()
            while True:
                try:
                    data["tahun_terbit"] = int(input("Tahun terbit: ").strip())
                    break
                except ValueError:
                    print("Masukkan tahun terbit yang valid!")
            data_buku.append(data)
            print("Buku berhasil ditambahkan!")

        # Menampilkan daftar buku
        elif keyword == 2:
            if not data_buku:
                print("Tidak ada data buku.")
            else:
                for i, databook in enumerate(data_buku, 1):
                    print(f"\nBuku ke-{i}")
                    print(f"Judul: {databook['judul']}")
                    print(f"Penulis: {databook['penulis']}")
                    print(f"Tahun Terbit: {databook['tahun_terbit']}")

        # Mencari buku berdasarkan judul
        elif keyword == 3:
            cari = input("Masukkan judul buku yang dicari: ").strip().lower()
            buku_ditemukan = [buku for buku in data_buku if buku["judul"].strip().lower() == cari]
            if buku_ditemukan:
                buku = buku_ditemukan[0]
                print(f"\nJudul: {buku['judul']}\nPenulis: {buku['penulis']}\nTahun Terbit: {buku['tahun_terbit']}")
            else:
                print("Buku tidak ditemukan!")

        # Menghapus buku berdasarkan judul
        elif keyword == 4:
            cari = input("Masukkan judul buku yang ingin dihapus: ").strip().lower()
            for i, buku in enumerate(data_buku):
                if buku["judul"].strip().lower() == cari:
                    data_buku.pop(i)
                    print("Buku berhasil dihapus!")
                    break
            else:
                print("Buku tidak ditemukan!")

        # Memperbarui informasi buku berdasarkan judul
        elif keyword == 5:
            cari = input("Masukkan judul buku yang ingin diperbarui: ").strip().lower()
            for buku in data_buku:
                if buku["judul"].strip().lower() == cari:
                    print("Masukkan data baru (tekan Enter untuk melewati perubahan)")
                    judul_baru = input(f"Judul ({buku['judul']}): ").strip()
                    penulis_baru = input(f"Penulis ({buku['penulis']}): ").strip()
                    try:
                        tahun_baru = input(f"Tahun Terbit ({buku['tahun_terbit']}): ").strip()
                        if tahun_baru:
                            tahun_baru = int(tahun_baru)
                        else:
                            tahun_baru = buku["tahun_terbit"]
                    except ValueError:
                        print("Tahun terbit tidak valid, perubahan dibatalkan.")
                        continue
                    buku["judul"] = judul_baru if judul_baru else buku["judul"]
                    buku["penulis"] = penulis_baru if penulis_baru else buku["penulis"]
                    buku["tahun_terbit"] = tahun_baru
                    print("Informasi buku berhasil diperbarui!")
                    break
            else:
                print("Buku tidak ditemukan!")

        # Menampilkan jumlah total buku
        elif keyword == 6:
            print(f"Total jumlah buku: {len(data_buku)}")

        # Keluar dari program
        elif keyword == 7:
            print("Keluar dari program...")
            break

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
# 