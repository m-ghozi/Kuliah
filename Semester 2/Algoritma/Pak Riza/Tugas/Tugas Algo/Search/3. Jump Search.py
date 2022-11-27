# Python3 code to implement Jump Search
from timeit import default_timer as timer
import math


def jumpSearch(arr, x, n):

    # Menemukan ukuran blok yang akan dilompat
    step = math.sqrt(n)

    # Menemukan blok tempat elemen berada
    # Jika ada
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Melakukan pencarian linier untuk x
    # blok dimulai dengan sebelum nya.
    while arr[int(prev)] < x:
        prev += 1

        # Jika kita mencapai blok berikutnya atau akhir
        # pada array, elemen tidak di temukan
        if prev == min(step, n):
            return -1

    # jika element di temukan
    if arr[int(prev)] == x:
        return prev

    return -1


# Kode untuk menguji fungsi
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 21
n = len(arr)

# menemukan indeks 'x' menggunakan Jump Search
start = timer()
index = jumpSearch(arr, x, n)
end = timer()
# Print  index dimana lokasi 'x'
print("Number", x, "is at index", "%.0f" % index)

print("Dalam waktu %10.7f detik" % (end-start))
