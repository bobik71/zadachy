a = int(input())
s = 0
k = 0
a1 = a
for i in range(1,a):
    if a % i == 0 and i % 2 == 1:
        s = s + i
print(s)
while a > 0:
    w = a % 10
    a = a // 10
    if w % 2 == 0:
        k = k + w
print(s + k)
