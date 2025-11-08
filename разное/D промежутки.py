n = int(input())
a = map(int,input().split())
a = list(a)
m = int(input())
b = []
for i in range(m):
    r,q = map(int,input().split())
    s = 0
    for ii in a:
        if r <= ii <= q:
            s += 1
    b.append(s)
for i in range(m):
    print(b[i])