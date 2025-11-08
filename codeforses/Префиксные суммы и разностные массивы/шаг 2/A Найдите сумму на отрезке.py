n = int(input())
a = list(map(int,input().split()))
b = [0]*(n+1)
q = int(input())

for i in range(n):
    b[i+1] = b[i]+a[i]

for i in range(q):
    l, r = map(int,input().split())
    print(b[r]-b[l-1])