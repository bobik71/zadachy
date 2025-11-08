n = [0, 0, 0, 0]

while n != [1, 1, 1, 1]:
    i = len(n)-1
    while n[i] != 0:
        n[i] = 0
        i -= 1
    n[i] = 1
    print(n)