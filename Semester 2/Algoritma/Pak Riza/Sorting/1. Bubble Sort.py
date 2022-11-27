from timeit import default_timer as timer


def susun_balon(list_awal):
    start = timer()
    # menghitung jumlah item dari list_awal
    for jumlah_awal in range(len(list_awal)-1, 0, -1):
        for data_ke in range(jumlah_awal):  # menentukan index ke dari jumlah_item
            # membandingkan item pertama dari list_awal dengan data setelahnya
            if list_awal[data_ke] > list_awal[data_ke+1]:
                # jika list_awal index ke 0 besar dari list_awal index setelahnya maka item dari list_awal index 0 akan dimasukan ke dalam variabel sementara
                sementara = list_awal[data_ke]
                # lalu item dari list_awal index ke 0 dimasukan ke dalam list_awal index setelahnya
                list_awal[data_ke] = list_awal[data_ke+1]
                # lalu nilai dari list_awal index setelahnya diganti dengan sementara
                list_awal[data_ke+1] = sementara
                # print("Sortiran ke", data_ke, list_awal)
    end = timer()
    return list_awal, end-start


list_angka = [5, 1, 3, 2, 7, 4, 6, 9, 8]
print(list_angka, "= Sebelum")
print("%s = Setelah, dalam waktu%10.7f detik " % susun_balon(list_angka))
