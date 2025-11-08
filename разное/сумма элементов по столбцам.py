h = []
s = 0
k = []
for i in range(5):
    h.append(list(map(int,input().split())))

for j in range(4):
    for i in range(5):
        s += h[i][j]
    k.append(s)
    s = 0
print(*k)
