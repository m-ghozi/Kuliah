from timeit import default_timer as timer
start_time = timer()
l = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 21  # elemen yang dicari
idx = -1  # posisi elemen yang dicari

for i in range(len(l)):
    if l[i] == x:
        idx = i
        break

if idx == -1:
    print('Nilai ', x, 'tidak ditemukan')
else:
    print('Nilai', x, 'ditemukan pada indeks', idx)

print("Dalam waktu %10.7f detik" % (timer()-start_time))

# Baris Ketiga adalah deklarasi list dengan isi beberapa elemen.
# Baris keempat berisi elemen yang dicari.
# Variabel idx pada baris kelima untuk menandai posisi elemen bila ditemukan. Variabel ini diisi dengan nilai awal -1.
# Perintah perulangan pada baris 7 s.d 10 memeriksa tiap elemen pada list, kemudian setelah elemen ditemukan idx diisi dengan nilai i (indeks saat ini) dan perulangan dihentikan dengan perintah break.
# Pada baris 12 s.d 15, jika idx masih terisi dengan nilai -1, berarti nilai yang dicari tidak ditemukan pada list. Sebaliknya, berarti nilai yang dicari ditemukan pada indeks yang sama dengan nilai idx.
