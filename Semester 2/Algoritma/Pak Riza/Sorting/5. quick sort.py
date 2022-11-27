from timeit import default_timer as timer


def partition(l, r, nums):
    start = timer()
    # item yang terakhir akan jadi pivot
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # memindahkan value yang lebih kecil dari pivot ke depan
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # mengganti isi dari element terakhir dengan index yg ditunjuk
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr, timer()-start


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        # Mengurutkan isi yang dikananan secara berulang
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)  # Mengurutkan isi yang dikiri secara berulang
    return nums


# menentukan nilai awal dari variabel data_list
data_list = [5, 3, 1, 2, 7, 4, 6, 9, 8]
# menampilkan isi dari variabel array yang belum di sort
print("Data yang akan di short :", data_list)
# menampilkan isi dari variabel array setelah dilakukan sorting
print("Data setelah di sort :", quicksort(0, len(data_list)-1, data_list))
