belanja = int(input('Total belanja Rp.'))

if belanja > 50000:
    print('Selamat anda mendapatkan diskon 5%')
    diskon = belanja * 5/100
    bayar = belanja - diskon

    print('Total belanja anda    Rp. ', belanja)
    print('Potongan harga        Rp. ', diskon)
    print('Anda cukup bayar      Rp. ', bayar)
print("Terimakasih sudah belanja")