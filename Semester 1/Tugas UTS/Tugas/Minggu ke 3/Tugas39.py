a = int(input('Masukkan bilangan ganjil lebih dari 35: '))

while a % 2 != 1 or a <= 35:
    a = int(input('Salah, masukkan lagi: '))
print('Benar')