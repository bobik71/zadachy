a = int(input())
d = []
for i in range( 
    while a > 0:
        o = a % 10
        d.append(o)
        a = a // 10
    f = len(d)
    for i in range(f-1):
        if d[i+1] > d[i]:
            exit()

