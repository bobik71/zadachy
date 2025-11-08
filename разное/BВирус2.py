n = int(input())
g = []
d = 0

for i in range(n):
    a = input()
    g.append(a[0])

for i in g:
    s = 0
    for j in g:
        if i == j:
            s += 1
            if s > d:
                d = s
                i1 = i

print(d,i1)