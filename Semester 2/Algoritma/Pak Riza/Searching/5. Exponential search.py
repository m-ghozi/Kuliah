# Python program to find an element x
# in a sorted array using Exponential Search

# Fungsi pencarian biner rekursif mengembalikan lokasi x dalam array yang diberikan arr[l..r] ada, jika tidak -1
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2  # menetukan posisi tengan dari array

        # jika elemen berada di tengah
        if arr[mid] == x:
            return mid

        # jika elemen kecil dari nilai mid, maka x pasti berada di subarray kiri
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Jika tidak, maka x pasti berada di subarray kanan
        return binarySearch(arr, mid + 1, r, x)

    # Jika x tidak ditemukan maka baris dibawah akan dijalankan
    return -1

# Returns the position of first occurrence of x in array


def exponentialSearch(arr, n, x):
    # Jika x berada di index pertama
    if arr[0] == x:
        return 0

    # mencari range untuk melakukan binary search
    i = 1
    # selama i kecil dari n dan array index ke i kecil sama dengan x
    while i < n and arr[i] <= x:
        i = i * 2  # untuk menemukan range

    # memanggil binary search untuk range yang telah ditemukan
    return binarySearch(arr, i // 2,
                        min(i, n-1), x)


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 21  # angka yang akan dicari
hasil = exponentialSearch(arr, n, x)
if hasil == -1:  # akan ditampilkan jika elemen tidak ditemukan
    print("Element tidak ditemukan pada array")
else:
    # akan ditampilkan ketika nilai x ditemukan
    print("Element %d berada di index %d  " % (x, hasil))
