n, m = map(int, input().split())
if m % n != 0:
    print(-1)
else:
    k = m // n
    s = 0   
    while k > 1:
        if k % 3 == 0:
            k //= 3
        elif k % 2 == 0:
            k //= 2
        else:
            print(-1)
            exit()
        s += 1
    else:
        print(s)
