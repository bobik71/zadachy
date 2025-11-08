a, b, c = map(int,input().split())
max = max(a, b ,c)
s = 0
e = []

for i in (a,b,c):
    if i % 2 == 0:
        s += 1

if s == 3:
    if a >= b >= c:
        print(a,b,c, sep = '')
    elif a >= c >= b:
        print(a,c,b, sep = '')
    elif b >= a >= c:
        print(b,a,c, sep = '')
    elif b >= c >= a:
        print(b,c,a, sep = '')
    elif c >= a >= b:
        print(c,a,b, sep = '')
    elif c >= b >= a:
        print(c,b,a, sep = '')

if s == 2:
    if a % 2 == 0 and b % 2 == 0:
        if b >= c >= a:
            print(b,c,a, sep = '')
        elif b >= a >= c:
            print(b,c,a, sep = '')
        elif a >= b >= c:
            print(a,c,b, sep = '')
        elif a >= c >= b:
            print(a,c,b, sep = '')
    if b % 2 == 0 and c % 2 == 0:
        if b >= a >= c:
            print(b,a,c, sep = '')
        elif b >= c >= a:
            print(b,a,c, sep = '')
        elif c >= a >= b:
            print(c,a,b, sep = '')
        elif c >= b >= a:
            print(b,a,c, sep = '')
    if c % 2 == 0 and a % 2 == 0:
        if c >= a >= b:
            print(c,b,a, sep = '')
        elif c >= b >= a:
            print(c,b,a, sep = '')
        elif a >= b >= c:
            print(a,b,c, sep = '')
        elif a >= b >= c:
            print(a,b,c, sep = '')
    
if s == 1:
    if a % 2 == 0:
        if b >= c:
            print(b,c,a, sep = '')
        else:
            print(c,b,a, sep = '')
    if b % 2 == 0:
        if a >= c:
            print(a,c,b, sep = '')
        else:
            print(c,a,b, sep = '')
    if c % 2 == 0:
        if b >= a:
            print(c,b,a, sep = '')
        else:
            print(c,a,b, sep = '')  