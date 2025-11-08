n, f = map(int, input().split())
r = []
for i in range(n):
    s = 0
    k, l = map(int, input().split())
    if k > l:
        s = l
    elif k < l:
        s = k
    elif k == l:
        s = l
    r.append(s)
g = []
h = r
m = r[0]
s1 = 0
for i in range(n):
    if m <= r[i]:
        m = r[i]
        g.append(m)
print(m,s1,g,r)
y = []
for i in range(f):
    t = max(g)
    y.append(t)
    del g[t]
print(y)
