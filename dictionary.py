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

data_mahasiswa = {
    "nama" : "Bagus",
    "umur" : 21,
    "jurusan" : "Informatika"
}
data_mahasiswa["alamat"] = "jakarta"
data_mahasiswa["umur"] = 22
del data_mahasiswa["alamat"]
cek_key = "nama" in data_mahasiswa
key_all = data_mahasiswa.keys()
values_all = data_mahasiswa.values()

print(data_mahasiswa)
print(cek_key)
print(key_all)
print(values_all)