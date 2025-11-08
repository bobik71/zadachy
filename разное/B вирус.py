n = int(input())
p = []

for si in range(n):
    s = input()
    k = len(s)
    z = s[:1]
    p.append(z) 
h = []
e = 0

for i in p:
    for si in range(len(p)):
        if p[si] == i:
            e += 1
    h.append(e)
    e = 0
print(h)
max = h[0]
g = 0
for i in range(len(h)):
    if max < h[i]:
        max = h[i]
        g = i
print(p[g],g)


