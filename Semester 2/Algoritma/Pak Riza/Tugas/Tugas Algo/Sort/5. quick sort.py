# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

from timeit import default_timer as timer


def partition(l, r, nums):
    # elemen terakhir akan menjadi pivot dan elemen pertama adalah pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Menukar nilai yang lebih kecil dari pivot ke depan
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Terakhir menukar elemen akhir dengan nomor indeks pointer
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

# Dengan fungsi quicksort(), kita akan menggunakan kode di atas
# untuk mendapatkan pointer di mana nilai kiri semuanya lebih kecil
# dari nilai kanan pada indeks pointer


def quicksort(l, r, nums):
    if len(nums) == 1:  # Mengakhiri kondisi untuk pengulangan. SANGAT PENTING
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Mengurutkan nilai kiri secara berulang
        quicksort(pi+1, r, nums)  # Mengurutkan nilai kanan secara berulang
    return nums


data_list = [21, 11, 24, 78, 1, 67, 13, 19, 40]
print("Data yang akan di short :", data_list)
start = timer()
quicksort(0, len(data_list)-1, data_list)
end = timer()
print("Data setelah di sort :", data_list)
print("Dalam waktu %10.7f detik" % (end-start))
