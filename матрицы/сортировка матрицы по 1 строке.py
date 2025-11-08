n = int(input())
m = int(input())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))

for j in range(m-1):
    for i in range(m-1):
        if s[0][i] < s[0][i+1]:
            b = s[0][i+1]
            s[0][i+1] = s[0][i]
            s[0][i] = b
            b1 = s[1][i+1]
            s[1][i+1] = s[1][i]
            s[1][i] = b1

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()
