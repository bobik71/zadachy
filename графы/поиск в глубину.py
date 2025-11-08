def pvg(q):
    a = [q]
    b = [0]*(n+1)
    b[q] += 1
    e = False
    print(q)
    while len(a) != 0:
        k = a[len(a)-1]
        for i in range(1,n+1):
            if s[k][i] == 1 and b[i] == 0:
                a.append(i)
                print(i)
                b[i] = 1
                e = True
                break
            e = False
        if e == False:
            a.pop()


n = int(input())
m = int(input())
s = [None]*(n+1)
for i in range(n+1):
    s[i] = []
for i in range(m):
    a,b = map(int,input().split())
    s[a].append(b)
    s[b].append(a)
#pvg(1)
print(s)