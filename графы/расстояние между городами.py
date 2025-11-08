def pvsh(q):
    a=[]
    z=[0]*(n+1)
    z[q] = 1
    b=[0]*2
    b[0]=q
    b[1]=0
    a.append(b)
    while len(a) != 0:
        k = a.pop(0)
        for i in range(1,n+1):
            if s[k[0]][i] == 1 and z[i] == 0:
                b = b.copy()
                b[0] = i
                z[i] = 1
                b[1] = k[1]+1
                a.append(b)
                if i == m1:
                    print(k[1]+1)
                    return

n = int(input())
m = int(input())
n1 = int(input())
m1 = int(input())
s1 = [0]*(n+1)
s = []
for i in range(n+1):
    s.append(s1.copy())
for i in range(m):
    a,b = map(int,input().split())
    s[a][b] += 1
    s[b][a] += 1
pvsh(n1)