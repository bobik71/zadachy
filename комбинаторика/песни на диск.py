disk = int(input())
p = list(map(int,input().split()))
res = 0
d = disk
n = [0]*4
a = []

while n != [1]*4:
    i = len(n)-1
    while n[i] != 0:
        n[i] = 0
        i -= 1
    n[i] = 1
    res = 0
    a = []
    for j in range(len(n)):
        if n[j] == 1:
            res+=p[j]
            a.append(p[j])
    if res < disk:
        if disk-res<d:
            d = disk - res
            ad = a
print(d)
print(ad)