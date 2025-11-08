n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    j = f[i] - 1
    k = f[j] - 1
    l = f[k] - 1
    if l == i:
        print("YES")
        break
else:
    print("NO")