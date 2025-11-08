def pm(a):
    for i in range(2,a):
        if a % i == 0:
            return 0
    return 1
def kpd(o):
    s = 0
    for i in range(2,o+1):
        if o % i == 0 and pm(i) == 1:
            s += 1
    return s
n, k = map(int,input().split())
w = map(int,input().split())
w = list(w)
s = 0
for i in w:
    if kpd(i) == k:
        s += 1
print(s)