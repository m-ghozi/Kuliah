ListMakanan = [
    'Rendang', 'Nasi Goreng', 'Pecel',
    'Sambalado', 'Ikan Bakar', 'Mie Instan'
]

MakananYangDicari = input('Masukkan nama makanan yang dicari ')

i = 0
while i < len(ListMakanan):
    if ListMakanan[i].lower() == MakananYangDicari.lower():
        print('Ketemu di index', i)
        break

    print('Bukan', ListMakanan[i])
    i += 1