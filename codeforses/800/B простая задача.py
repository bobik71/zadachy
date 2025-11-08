for i in range(int(input())):
    a = input()
    b = ''

    for i in range(len(a)):
        if a[i] == 'p':
            b += 'q'
        if a[i] == 'q':
            b += 'p'
        if a[i] == 'w':
            b += 'w'
print(b[::-1])