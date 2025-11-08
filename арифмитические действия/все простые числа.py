n = 50000
s = 0
q = []

for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            s += 1
    if s == 0:
        q.append(i)
    s = 0
print(q)