def countingSort(arr, exp1):

    n = len(arr)

    output = [0] * (n)

    # inisialisasi index dengan 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index) % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    # Membuat output array
    i = n-1
    while i >= 0:
        index = (arr[i]/exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # menyalin isi dari output array ke arr
    # sekarang arr berisi angka yang telah disortir
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method untuk radix sort
def radixSort(arr):

    # Mencari angka terbesar
    max1 = max(arr)

    # melakukan counting sort untuk setiap angka
    # dimana i adalah angka terbaru
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10


data_list = [5, 3, 1, 2, 7, 4, 6, 9, 8]
print("Data awal :", data_list)
radixSort(data_list)

print("Data setelah di sort :")
for i in range(len(data_list)):
    print(data_list[i], end=" ")
