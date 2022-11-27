from timeit import default_timer as timer
start = timer()
l = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
dicari = 21
print('Mencari nilai', dicari, 'dengan binary search', 'pada list', l)
ditemukan = False
batas_awal = 0
batas_akhir = len(l) - 1
while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir-batas_awal)//2  # ambil posisi tengah
    print('posisi pencarian: index', pos_cari, 'dengan nilai', l[pos_cari])
    if l[pos_cari] == dicari:
        ditemukan = True
    elif l[pos_cari] > dicari:
        batas_akhir = pos_cari-1  # geser 1 titik lebih kecil dari posisi sekarang
    else:
        batas_awal = pos_cari+1  # geser 1 titik lebih besar dari posisi sekarang

if ditemukan:
    print('Nilai', dicari, 'ditemukan pada indeks', pos_cari)
else:
    print('Nilai', dicari, 'tidak ditemukan')
end = timer()
print("Dalam waktu %10.7f detik" % (end-start))

# List dimana pencarian dilakukan memiliki 18 elemen
# Pencarian elemen (nilai 7) sampai akhirnya ditemukan, dilakukan dalam empat iterasi sbb:
# Pada iterasi pertama, batas awal pencarian ada pada elemen dengan indeks 0, batas akhir ada pada elemen dengan indeks 17. Posisi pencarian diambil dari tengah-tengah kedua batas (17-0)/2 = 8. Pada indeks 8 ditemukan elemen bernilai 14. Nilai elemen ini lebih besar dari nilai yang dicari, oleh karena itu batas akhir pencarian digeser pada posisi pencarian saat ini dikurangi 1.
# Pada iterasi kedua batas awal dan akhir menjadi 0 dan 7, posisi tengah didapatkan pada indeks 3. Pada indeks ini ditemukan elemen bernilai 6, ini berarti bahwa batas awal perlu dinaikkan ke posisi pencarian saat ini ditambah 1.
# Pada iterasi ketiga batas awal dan akhir menjadi 4 dan dan 7, posisi tengah didapatkan pada indeks 5. Pada indeks ini ditemukan elemen bernilai 8, ini berarti batas akhir kembali diturunkan ke indeks 4 (5-1)
# Pada iterasi ke 4, batas awal dan akhir menjadi 4 dan 4, posisi tengah pada indeks 4, dan ditemukan elemen bernilai 7.
