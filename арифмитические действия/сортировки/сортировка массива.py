a = map(int,input().split())
a = list(a)
for j in range(len(a)-1):
    m = a[j]
    n = j
    for i in range(j,len(a)):
        if a[i] < m:
            m = a[i]
            n = i
    a[n] = a[j]
    a[j] = m
print(a)

