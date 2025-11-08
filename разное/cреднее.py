a = int(input())
a1 = a
z = 0
s = 0
while a > 0:
    k = a % 10
    z = z + 1
    a = a // 10
u = z // 2 + 1
while a1 > 0:
    k = a1 % 10
    s = s + 1
    if s == u:
        print(k)
    a1 = a1 // 10
    
