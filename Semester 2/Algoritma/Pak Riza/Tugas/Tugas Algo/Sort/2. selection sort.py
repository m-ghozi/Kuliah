from timeit import default_timer as timer


def selection_sort(list_saya):
    start = timer()
    # menghitung jumlah item yg akan disortit dalam variabel list_saya
    for i in range(len(list_saya)-1):
        # menentukan index terendah dari i, diasumsikan bahwa index pertama adalah yang terkecil
        index_minimum = i
        dex = 0
        # menggunakan j untuk melakukan loop ke elemen yang tersisa
        for j in range(i+1, len(list_saya)):
            # membandingkan isi list_saya index ke j, dengan index minimum di list_saya
            if list_saya[j] < list_saya[index_minimum]:
                index_minimum = j  # mengganti isi dari index_minimum dengan index ke j dari list_saya
        # setelah menemukan index minimum dari list yang belum disusun, lalu menggantinya dengan item pertama yg belum disortir
        list_saya[i], list_saya[index_minimum] = list_saya[index_minimum], list_saya[i]
    end = timer()
    return list_saya, end-start


# menentukan isi list dari variabel thelist
thelist = [5, 3, 1, 2, 7, 4, 9, 6, 8]
print(thelist, "= Sebelum")

print("%s = Setalah, Dalam waktu%10.7f detik" % selection_sort(thelist))
