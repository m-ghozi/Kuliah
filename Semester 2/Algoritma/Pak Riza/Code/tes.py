s = 5
q = 1
for x in range(1, 6 + 1, 1):
    for y in range(1, q + 1, 1):
        for i in range(0, s + 1, 1):
            print(" ", end='', flush=True)
        print("*", end='', flush=True)
        s = -1
    print("")
    s = 5 - x
    q = x * 2 + 1
