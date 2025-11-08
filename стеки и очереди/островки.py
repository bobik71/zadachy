n, m = map(int,input().split())
s = []
x = []
y = []
os = 0
for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            x.append(i)
            y.append(j)
            os += 1
        while x:
            k1 = x.pop(0)
            k2 = y.pop(0)
            s[k1][k2] = 0
            if k1 + 1 < n:
                if s[k1+1][k2] == 1:
                    x.append(k1+1)
                    y.append(k2)
                    s[k1+1][k2] = 0

            if k1 - 1 >= 0:
                if s[k1-1][k2] == 1:
                    x.append(k1-1)
                    y.append(k2)
                    s[k1-1][k2] = 0

            if k2 + 1 < m:
                if s[k1][k2+1] == 1:
                    x.append(k1)
                    y.append(k2+1)
                    s[k1][k2+1] = 0

            if k2 - 1 >= 0:
                if s[k1][k2-1] == 1:
                    x.append(k1)
                    y.append(k2-1)
                    s[k1][k2-1] = 0

print(os)