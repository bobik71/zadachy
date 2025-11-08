s = 0
b = 0
a1 = int(input())
a2 = a1
a3 = a1
n = a3 % 10
while a1 > 0:
    k = a1 % 10
    b = b + 1
    a1 = a1 // 10
z = b // 2
while a2 > 0:
    k = a2 % 10
    s = s + 1
    a2 = a2 // 10
    if s == b - z:
        print(k)   
