a = int(input())
if a % 10 != 0:
    print(1, a)
else:
    a1 =a
    while a % 10 == 0:
        a = a // 2
    print(a,a1//a)
