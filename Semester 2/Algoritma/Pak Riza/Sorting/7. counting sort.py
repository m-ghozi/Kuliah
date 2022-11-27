from timeit import default_timer as timer


def counting(data):
    start = timer()
    counts = [0 for i in range(max(data)+1)]

    for value in data:
        counts[value] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]

    arr = [0 for loop in range(len(data))]
    for value in data:
        index = counts[value] - 1
        arr[index] = value
        counts[value] -= 1
    end = timer()
    return arr, end-start


data = [5, 3, 1, 2, 7, 4, 6, 9, 8]
print(data, "= Sebelum")
print("%s = Setelah, Dalam waktu%10.7f detik" % counting(data))
