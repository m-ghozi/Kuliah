total = int(input('Total belanja : Rp. '))
if total > 100000:
    print("Bonus Bimoli 1L")
elif total >= 90000:
    print("Bonus Bimoli 200ml")
elif total >= 80000:
    print("Bonus Bimoli 100ml")
else:
    print("Tidak ada Bonus")