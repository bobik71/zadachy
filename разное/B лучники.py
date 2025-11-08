n, l, r, a, b = map(int, input().split())
o = 0
for i in range(l,r+1):
    if i != a and i != b:
        o = o + 1
print(o)       
