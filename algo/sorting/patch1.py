# import json
# import time
# import random


# with open("D:/backup data 2023/optional/belajar python/algo/sorting/data.json", "r") as f:
#         dataa = json.load(f)

# hasil = list(dataa.keys())

# tahun_terbit_list = [buku["tahun_terbit"] for buku in dataa.values()]


# print(tahun_terbit_list)


# data = tahun_terbit_list
# def insertion_sort(data):
#     a = 0
#     waktuM = time.time()
#     for i in range(1, len(data)): # perulangan pertama
#         key_item = data[i] # ini elemen yang akan kita posisikan
#         j = i - 1 # kunci index posisi
#         while j >= 0 and data[j] > key_item: # lakukan perulangan kedua
#             data[j + 1] = data[j] # menggeser elemen yang lain
#             j -= 1
#             data[j + 1] = key_item # memposisikan elemen
#             print(f"step ke-{a} : {data}, iterasi ke-{i}")
#             a += 1

#     waktuS = time.time()
#     waktuA = waktuS - waktuM
#     print(f'Waktu : {waktuA:.6f}' )

#     return data

# print("Hasil dari Insertion Sort adalah ",insertion_sort(data))
import datetime
import json
import time
from prettytable import PrettyTable

with open("\\Users\\Lenovo\\Documents\\Algoritma Dasar\\Tugas AKhir\\2\\data.json", "r") as f:
    dataa = json.load(f)

rating = [buku["rating"] for buku in dataa.values()]
nama = [buku for buku in dataa.keys()]
tutup = [buku["jam tutup"] for buku in dataa.values()]

import datetime
now = datetime.datetime.now().time()

status_awal = []

for restaurant, info in dataa.items():
    jam_buka = datetime.datetime.strptime(info["jam buka"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()
    jam_tutup = datetime.datetime.strptime(info["jam tutup"], "%H:%M").replace(tzinfo=datetime.timezone.utc).time()

    if jam_buka <= now <= jam_tutup:
        status = "buka"
    else:
        status = "tutup"

    status_awal.append(status)
    

data = list(dataa.items())

def insertion_sort(data):
    a = 0
    waktuM = time.time()
    for i in range(1, len(data)):  
        key_item = data[i]  
        j = i - 1  
        while j >= 0 and data[j][1]["rating"] < key_item[1]["rating"]:  
            data[j + 1] = data[j]  
            j -= 1
        data[j + 1] = key_item  
        print(f"step ke-{a} : {[buku[1]['rating'] for buku in data]}, iterasi ke-{i}")
        a += 1

    waktuS = time.time()
    waktuA = waktuS - waktuM
    print(f'Waktu : {waktuA:.6f}')

    return data

sorted_data = insertion_sort(data)

print("\nWarung sebelum di sorting")
tabel = list(zip(nama, rating, status_awal, tutup))

table1 = PrettyTable()
table1.field_names = ["nama warung", "rating", "status", "jam tutup"]
for buku in tabel:
    table1.add_row(buku)
print(table1)

print("\nWarung setelah di sorting by rating")

table = PrettyTable()

table.field_names = ["nama warung", "rating", "status", "jam tutup"]
for buku in sorted_data:
    jam_buka = datetime.datetime.strptime(buku[1]['jam buka'], "%H:%M").time()
    jam_tutup = datetime.datetime.strptime(buku[1]['jam tutup'], "%H:%M").time()
    if jam_buka <= now <= jam_tutup:
        status = "buka"
    else:
        status = "tutup"
    table.add_row([buku[0], buku[1]['rating'], status, buku[1]['jam tutup']] )
print(table)
