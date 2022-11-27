import random

'''
arr : nama variabel yg akan disortir
start : memulai index dari array
stop : mengakhiri index dari array
'''


def quicksort(arr, start, stop):
    if(start < stop):

        # pivorindex adalah dimanan index berada
        pivotindex = partitionrand(arr, start, stop)

        quicksort(arr, start, pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)


def partitionrand(arr, start, stop):

    # Menghasilkan angka acak antara index awal dan index akhir
    randpivot = random.randrange(start, stop)

    # mengganti nilai awal dari array dengan pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start

    i = start + 1

    for j in range(start + 1, stop + 1):

        # ketika elemen terbaru kecil atau sama dengan pivot, maka akan digeser ke sisi kiri dari partition
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] =\
        arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)


array = [5, 3, 1, 2, 7, 4, 6, 9, 8]
print("Data yang akan di short :", array)
quicksort(array, 0, len(array) - 1)
print("Data setelah di sort :", array)
