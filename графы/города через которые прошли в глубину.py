def rpvg(q):
    global lst_pr
    lst_pr.append(q)
    z[q] = 1

    for i in range(1,n+1):
        if s[q][i] == 1 and z[i] == 0:
            if i == m1:
                lst_pr.append(i)
                print(*lst_pr)
                exit()
            else:    
                rpvg(i)
        elif i == n:
            lst_pr = []
            rpvg(n1)



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
z = [0]*n
lst_pr = []
rpvg(n1)