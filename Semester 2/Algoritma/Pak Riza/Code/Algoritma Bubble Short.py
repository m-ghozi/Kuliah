def susun_gelembung(list_angka):
    for angka_ke in range(len(list_angka)-1, 0, -1):
        for index_ke in range(angka_ke):
            if list_angka[index_ke] > list_angka[index_ke+1]:
                sementara = list_angka[index_ke]
                list_angka[index_ke] = list_angka[index_ke+1]
                list_angka[index_ke+1] = sementara


cobalist = [5, 3, 1, 2, 4, 6, 8, 9]
susun_gelembung(cobalist)
print(cobalist)
