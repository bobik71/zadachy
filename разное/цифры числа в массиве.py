a = []
k = int(input())
while k > 0:
    b = k % 10
    a.append(b)
    k = k // 10
print(a)
