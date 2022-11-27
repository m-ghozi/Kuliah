listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
    'Jogjakarta', 'Payokumbuah', 'Padang'
]

# skip jika i adalah bilangan genap
# dan i lebih dari 0
i = -1
while i < len(listKota):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue
    # tidak dieksekusi ketika continue dipanggil
    print(listKota[i])