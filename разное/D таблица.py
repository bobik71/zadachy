n, m = map(int, input().split())
b = []
s = 0
for i in range(n):
    a = map(int, input().split())
    a = list(a)
    maxa = max(a)
    b.append(maxa)
maxb = max(b)
for i in range(n):
    if maxb == b[i]:
        s += 1
print(n - s)
