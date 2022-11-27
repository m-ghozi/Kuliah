# Python3 program to implement
# interpolation search
# with recursion

# Jika x ada di arr[0..n-1], maka
# mengembalikan indeksnya, jika tidak maka di kembalikan ke -1.
from timeit import default_timer as timer
from turtle import clear


def interpolationSearch(arr, lo, hi, x):

    # Karena array diurutkan, sebuah elemen hadir dalam array harus dalam rentang sudut yang di tentukan
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

        # Menyelidiki posisi dengan menjaga
        # kesamaan distribusi di mind.
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))

        # ketika kondisi target di temukan maka akan melakukan
        if arr[pos] == x:
            return pos

        # Jika x lebih besar dan  x berada di sub array kanan
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)

        # Jika x lebih kecil dan x ada di sub array kiri
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1

# contoh code


# Dimana pencarian item array akan di lakukan

arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

# Elemen yang akan dicari
x = 21
start = timer()
index = interpolationSearch(arr, 0, n - 1, x)
end = timer()
# jika element di temukan maka print
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")  # jika element tidak ditemukan

print("Dalam waktu %10.7f detik" % (end-start))
