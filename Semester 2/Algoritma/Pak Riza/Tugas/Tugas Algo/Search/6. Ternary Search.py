# Function to perform Ternary Search
from timeit import default_timer as timer


def ternarySearch(left, right, key, ar):
    while right >= left:

        # mencari mid1 dan mid2
        # modulus 5 karena kita akan membagi ar menjadi ke 3 bagian jumlah ar adalah 15/3 = 5
        mid1 = left + (right-left) // 5
        mid2 = right - (right-left) // 5
        # mengecek jika key berada di mid
        if key == ar[mid1]:
            return mid1
        if key == mid2:
            return mid2

        # karena key tidak ditemukan di mid
        # maka check setiap bagian dari ar
        # Kemudian ulangi pencarian dibagian itu
        if key < ar[mid1]:
            # Key berada diantara left dan mid1
            right = mid1 - 1
        elif key > ar[mid2]:
            # key berada di antara mid2 dan right
            left = mid2 + 1
        else:
            # Key berada diantara mid1 dan mid2
            left = mid1 + 1
            right = mid2 - 1

    # key tidak ditemukan
    return -1


# Data yang telah disortir
ar = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]

# index awal
left = 0

# Panjang List
right = 14

# Angka yang akan dicari dalam list
key = 21
start = timer()
hasil = ternarySearch(left, right, key, ar)
end = timer()
if hasil == -1:  # akan ditampilkan jika elemen tidak ditemukan
    print("Element tidak ditemukan pada array")
else:
    # akan ditampilkan ketika nilai x ditemukan
    print("Element %d berada di index %d  " % (key, hasil))
print("Dalam waktu %10.7f detik" % (end-start))
