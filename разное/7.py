a = int(input())
a1 = a
s = 0
k = 0
while a > 0:
    s = s + 1
    a = a // 10
u = s // 2 + 1
while a1 > 0:
    k = k + 1
    l = a1 % 10
    if k == u:
        print(l)
    a1 = a1 // 10
        
