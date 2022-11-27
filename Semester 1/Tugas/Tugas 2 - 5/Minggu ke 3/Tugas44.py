#menggunakan while

DaftarAngka =[16,25,8,17,54,32,23]
lenght=len(DaftarAngka)-1
sorted=False

while not sorted:
    sorted=True
    for i in range(lenght):
        if DaftarAngka[i]>DaftarAngka[i+1]:
            DaftarAngka[i],DaftarAngka[i+1],[i]