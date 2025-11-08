from collections import deque

def pvsh(q):
    a = deque()
    b = [0]*(n+1)
    b[q] = 1
    a.append(q)
    k = q
    while len(a) != 0:
        k = a.popleft()
        print(k)
        for i in range(len(s[k])):
            if b[s[k][i]] == b[k] and s[k][i] != k:
                print('NO')
                exit()
            if b[s[k][i]] == 0:
                a.append(s[k][i])
                if b[k] == 1:
                    b[s[k][i]] = 2
                if b[k] == 2:
                    b[s[k][i]] = 1
                

n = int(input())
m = int(input())
s1 = [0]*(n+1)
s = [None]*(n+1)
for i in range(n+1):
    s[i] = []
for i in range(m):
    a,b = map(int,input().split())
    s[a].append(b)
    s[b].append(a)
pvsh(1)
print('YES')
