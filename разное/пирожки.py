w = []
q = []
s = 0
n, m = map(int,input().split())
for i in range(n):
    w.append(int(input()))
for i in range(m):
    q.append(int(input()))

for i in w:
    for j in q:
        if j < i:
            s += 1
            break

print(len(w)+s)