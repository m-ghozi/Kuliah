total = int(input("Total belanja : Rp. "))
if total > 100000:
    print("Anda mendapkan bonus Bimoli 1L")
if total > 90000:
    print("Anda mendapakan bonus Bimoli 200ml")
if total < 90000:
    print("Tidak ada bonus")