from timeit import default_timer as timer


def insertion_sort(array):
    start = timer()

    # Melakukan perulangan dari elemen ke dua sampai element terakhir
    for i in range(1, len(array)):
        # menyimpan array index ke i kedalam variabel key_item
        key_item = array[i]

        j = i - 1  # inisialisasi variabel yg akan digunakan untuk menemukan posisi index pembanding dengan key_item

        # melakukan perulangan selama nilai dari j ke besar atau sama dengan 0 dan membandingkan array index ke j dengan key_item
        while j >= 0 and array[j] > key_item:
            # ketika ketika value dari key_item kecil dari array index ke j maka akan menggeser satu item ke ke kiri
            # dan memposisikan j ke posisi index selanjutnya
            array[j + 1] = array[j]
            j -= 1  # menggeser index satu posisi ke kiri

        # menggeser kembali ke posisi key_item kelokasi yang benar, setelah selesai melakukan sorting
        array[j + 1] = key_item
    end = timer()
    return array, end-start


array = [5, 3, 1, 2, 7, 4, 9, 6, 8]  # memasukan nilai awal dari variabel array
# menampilkan isi dari variabel array yang belum di sort
print(array, "= Sebelum")
# menampilkan isi dari variabel array setelah dilakukan sorting
# for i in range(5):
print("%s = Sesudah, Dalam waktu%10.7f detik" % insertion_sort(array))
