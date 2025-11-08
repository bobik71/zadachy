n = int(input())
a = map(int,input().split())
a = list(a)
k = 0
a1 = [0] * n
for i in range(1,n):
    a1[i] = a[i-1]
a1[0] = a[n-1]
print(a1)