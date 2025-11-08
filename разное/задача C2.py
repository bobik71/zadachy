a, b, c = map(int,input().split())
p = 0
if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print(-1)
    exit()
if a % 2 == 0:
    if b != 0:
       s = int(str(b)+str(c)+str(a))
       if s > p:
           p = s
    if c != 0:
        s = int(str(c)+str(b)+str(a))
        if s > p:
           p = s

if b % 2 == 0:
    if a != 0:
        s = int(str(a)+str(c)+str(b))
        if s > p:
           p = s
    if c != 0:
        s = int(str(c)+str(a)+str(b))
        if s > p:
           p = s     

if c % 2 == 0:
    if b != 0:
        s = int(str(b)+str(a)+str(c))
        if s > p:
           p = s  
    if a != 0:
        s = int(str(a)+str(b)+str(c))
        if s > p:
           p = s  
print(p)