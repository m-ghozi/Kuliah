def qs(list, awal, akhir):
    if awal < akhir:
        pindex = partisi(list, awal, akhir)
        qs(list, awal, pindex-1)
        qs(list, pindex+1, akhir)


def partisi(list, awal, akhir):
    tengah = int(akhir/2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal, tengah):
        if list[i] >= pivot:
            list[i], list[pindex] = list[pindex], list[i]
            pindex = pindex + 1
    list[pindex], list[tengah] = list[tengah], list[pindex]
    print(list)
    return pindex


list = [67, 91, 87, 33, 49, 10, 16, 43, 65, 3]
print('Data yang akan di sort :', list)
print('Quick Sort :')
qs(list, 0, len(list)-1)
