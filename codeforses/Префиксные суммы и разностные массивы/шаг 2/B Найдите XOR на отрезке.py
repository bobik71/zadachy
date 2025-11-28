n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)

for i in range(n):
    b[i + 1] = b[i] ^ a[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(b[r] ^ b[l - 1])
