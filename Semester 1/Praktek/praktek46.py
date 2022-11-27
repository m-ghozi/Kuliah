listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi',
    'Solo', 'Jogjakarta', 'Payakumbuh', 'Padang'
]

KotaYangDicari = input("Ketik Nama kota yang kamu cari :  ")

for i, kota in enumerate(listkota):
    # kita ubah katanya ke lowercase agar
    # menjadi case insensitive
    if kota.lower() == KotaYangDicari.lower():
        print('Kota yang anda cari ada pada indeks', i)
        break
else:
    print('Maaf, kota yang anda cari tidak ada')