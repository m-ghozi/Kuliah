from timeit import default_timer as timer


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


array = [9, 5, 1, 4, 8, 7, 2, 3, 6]
print('Data awal :', array)
start = timer()
merge_sort(array)  # menjalankan fungsi yang telah dibuat
end = timer()
print('Data setelah di sort :', array)
print("Dalam waktu %10.7f detik" % (end-start))

# Data dipecah menjadi dua kelompok dimana kelompok pertama adalah setengah apabila data genap atau setengah kurang satu apabila data ganjil dari seluruh data.
# Kemudian dilakukan pemecahan kembali pada masing-masing kelompok hingga hanya terdapat satu data pada satu kelompok.
# Setelah digabungkan kembali dengan membandingkan pada blok yang sama apakah data pertama lebih besar dari pada data ketengah ditambah satu, jika iya maka data ketengah ditambah satu dipindah menjadi data pertama.
# Kemudian data pertama tadi hngga data ketengah dipindah menjadi data kedua sampai data ketengah ditambah satu.
# Begitu seterusnya sehingga membentuk sebuah data yang tersusun dalam satu kelompok yang utuh.
