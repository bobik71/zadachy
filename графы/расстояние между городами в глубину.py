def rpvg(q):
    if q[0] == m1:
        print(q[1])
        exit() 
    w[q[0]] = 1
    for i in range(1,n+1):
        if s[q[0]][i] == 1 and w[i] == 0:
            q=q.copy()
            q[0] = i
            q[1] = q[1]+1
            rpvg(q)

n = int(input())
m = int(input())
n1 = int(input())
m1 = int(input())
s1 = [0]*(n+1)
s = []
q = []
w=[0]*(n+1)
q.append(n1)
q.append(0)
for i in range(n+1):
    s.append(s1.copy())
for i in range(m):
    a,b = map(int,input().split())
    s[a][b] += 1
    s[b][a] += 1

rpvg(q)