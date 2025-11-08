n = int(input())
b = []
for i in range(n):
    a = map(int,input().split())
    a = list(a)
    b.append(max(a))
print(b)
