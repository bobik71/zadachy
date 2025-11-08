def sz(n):
    s = 0
    while n > 0:
        d = n % 10
        s += d
        n = n // 10
    return s
a = int(input())
print(sz(a))
s = 0
for i in range(1,a+1):
    d = sz(i)
    if d == 5:
        s += 1

print(s)