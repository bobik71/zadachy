n = int(input())
s = []
p = 0
p1 = 0
for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(n):
    for j in range(2):
        print(s[i][j], end = ' ')
    print()
