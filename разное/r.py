a = map(int,input().split())
a = list(a)
k = len(a)
s = 0
for i in range(k):
    if a[i] % 2 == 0:
        s = s + a[i]
print(s)
