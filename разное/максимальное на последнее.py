n = []
a = map (int,input().split())
a = list(a)
n = len(a)
m = a[0]
s1 = 0
for i in range(n):
    if m < a[i]:
        m = a[i]
        s1 = i
s2 = s1
x = a[n-1]
a[n-1] = a[s1]
a[s2] = x
print(a)
