# membuat list kosong unutk menampung hobi
hobi = []
stop = False
i = 0

# mengisi hobi
while (not stop):
    hobi_baru = input("Input hobi ke-{} :".format(i))
    hobi.append(hobi_baru)

    # Increment
    i += 1

    tanya = input("Mau isi lagi ga? (y/t): ")
    if(tanya == "t"):
        stop = True

# cetak semua hobi
print("=" * 10)
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
    print("- {}".format(hb))