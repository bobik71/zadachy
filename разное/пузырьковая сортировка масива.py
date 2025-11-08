a = map(int,input().split())
a = list(a)
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            b = a[i+1]
            a[i+1] = a[i]
            a[i] = b
print(a)

