n = int(input())
m = int(input())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))

for j in range(m):
    m = s[0][j]
    n = j
    for i in range(j,m):
        if s[0][i] < m:
            m = s[0][i]
            n = i
    s[0][n] = s[0][j]
    s[0][j] = m
    b = s[1][n]
    s[1][n] = s[1][j]
    s[1][j] = b

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()