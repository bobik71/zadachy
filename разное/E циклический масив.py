n ,k = map(int,input().split())
a = map(int,input().split())
a = list(a)
a1 = [0] * n
for i in range(k):
    for q in range(1,n):
        a1[q] = (a[q-1] + a[q]) % 1000000007
        a1[0] = (a[0] + a[n-1]) % 1000000007
    a = a1
    a1 = [0] * n
print(*a)