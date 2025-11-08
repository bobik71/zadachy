a, b, c = map(int,input().split())
a1 = a - b
if c - a1 <= 0:
    print('0')
    exit()
print(c - a1)
