"""
List Comprehension di Python
List comprehension adalah cara singkat untuk membuat list baru dari list yang sudah ada atau dari suatu iterable.

1.bentuk dasar:
    new_list = [expression for item in iterable]
"""

# angka1 = [i for i in range(1,11)]
# print(f"Angka 1 = {angka1}")
#
# print( "Angka 2 = " ,[i for i in range(3)])


"""
2. List Comprehension dengan Kondisi
    new_list = [expression for item in iterable if condition]
"""

# jika ingin membuat list angka 1-10 yang di ambil nilai genapnya.

# genap = [i for i in range(1,11) if i % 2 == 0]
# print(f"Angka genap: {genap}")

# atau jika untuk print saja.

# print("Angka ganjil: ", [i for i in range(1,11) if i % 2 == 1])


"""
3. List Comprehension dengan Else (Ternary Operator)
    new_list = [expression1 if condition else expression2 for item in iterable]

"""

# buat print saja.
# print("Angka status : ", ["genap" if i % 2 == 0 else "Ganjil" for i in range(3)])


"""
4. Nested List Comprehension (Bersarang)

"""
# print("List bersarang: ", [[i for i in range(1,4)] for _ in range(3)])

"""
Latihan:
Coba buat list yang berisi kuadrat dari angka ganjil antara 1-10 menggunakan list comprehension.
"""

# ganjil = [i**2 for i in range(1,11) if i % 2 == 1]
# print(ganjil)
#
# # versi print saja.
# print("Kuadrat Angka ganjil: ", [i ** 2 for i in range(1,10) if i % 2 == 1])

"""
Tantangan 1
Buat list comprehension yang menghasilkan bilangan genap antara 1-20 yang bukan kelipatan 4.
"""

angka = [i for i in range(1,21) if i % 2 == 0 and i % 4 != 0]
print(angka)