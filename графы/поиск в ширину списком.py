def pvsh(q):
    a = []
    b = [0]*(n+1)
    a.append(q)
    while len(a) != 0:
        k = a.pop(0)
        print(k)
        b[k] = 1
        for i in range(len(s[k])):
            if b[s[k][i]] == 0:
                a.append(s[k][i])

n = int(input())
m = int(input())
s = [None]*(n+1)
for i in range(n+1):
    s[i] = []
for i in range(m):
    a,b = map(int,input().split())
    s[a].append(b)
    s[b].append(a)
pvsh(1)
