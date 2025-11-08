a = list(map(int,input().split()))
n = int(input())
a1 = a[:n+1]

for i in range(len(a)-1, n, -1):
    a1.append(a[i])
print(a1)