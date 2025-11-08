n = int(input())
a = list(map(int,input().split()))
so = 0
sp = 0

for i in a:
    if i < 0:
        so += i
    if i > 0:
        sp += i

if sp + so == 0:
    print(sp)
else:
    print(-1)