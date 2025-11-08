a, b, c = map(int,input().split())
q = []
if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print(-1)
    exit()
if a != 0 and c % 2 == 0:
    s = int(str(a)+str(b)+str(c))
    q.append(s)
if a != 0 and b % 2 == 0:
    s = int(str(a)+str(c)+str(b))
    q.append(s)
if b != 0 and c % 2 == 0:
    s = int(str(b)+str(a)+str(c))
    q.append(s)
if b != 0 and a % 2 == 0:
    s = int(str(b)+str(c)+str(a))
    q.append(s)
if c != 0 and b % 2 == 0:
    s = int(str(c)+str(a)+str(b))
    q.append(s)
if c != 0 and a % 2 == 0:
    s = int(str(c)+str(b)+str(a))
    q.append(s)
print(max(q))