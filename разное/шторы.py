a, b = map(int, input().split())
p = 2 * b
if p >= a:
    u = 0
else:
    u = a - p
print(u)
