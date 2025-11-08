n = int(input())
g = list(map(int,input().split()))
s = 0
s1 = 0

for i in range(n):
    g[i] = int(format(g[i], 'b'))

for i in range(0,n-1):
    for j in range(i+1,n):
        d = g[i]+g[j]
        print(d)
        while d < 0:
            s += d % 2
            d = d // 2
        if s == 2:
            s1 += 1

print(s1)