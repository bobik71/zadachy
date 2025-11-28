n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
i1, j1, n1 = map(int,input().split())
i1 -=1
j1-=1

def pere(a):
    a1 = []
    for i in range(n1):
        a1.append([0]*n1)
    for i in range(i1,n1+i1):
        for j in range(j1,n1+j1):
            a1[i][j] = a[n-j-1][i]
    return a1

for i in range(n):
    for j in range(n):
        print(str(a[:i1])+' ' +str(pere(a)[i]))