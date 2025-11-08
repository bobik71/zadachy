def rpvg(q):
    print(q)
    for i in range(1,n+1):
        if b[i] == b[q] and i != q and s[q][i] == 1:
            print('NO')
            exit()
        if s[q][i] == 1 and b[i] == 0:
            if b[q] == 1:
                b[i] = 2
            if b[q] == 2:
                b[i] = 1
            rpvg(i)

          
n = int(input())
b = [0]*(n+1) 
m = int(input())
s1 = [0]*(n+1)
s = []
for i in range(n+1):
    s.append(s1.copy())
for i in range(m):
    a,x = map(int,input().split())
    s[a][x] += 1
    s[x][a] += 1
#for i in range(n):
    #print(s[i])
b[1] = 1
rpvg(1)
print('YES')