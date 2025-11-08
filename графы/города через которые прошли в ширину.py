def pvsh(q):
    a = []
    global z
    z = []
    r = [1,0]
    for i in range(n+1):
        if i == q:
            z.append(r)
        else:
            z.append([0,0])
    b = [0]*2   
    b[0] = q
    b[1] = 0
    a.append(b)   
    while len(a) != 0:
        k = a.pop(0)  
        
        if k[0] == m1:
            break
            
        for i in range(1, n+1):
            if s[k[0]][i] != 0 and z[i][0] == 0:
                z[i][0] = 1     
                z[i][1] = k[0]   
                b = [0]*2
                b[0] = i
                b[1] = k[0] + 1
                a.append(b)

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

z1 = [m1]
i = m1
t = 0
while z[i][1] != 0:
    z1.append(z[i][1])
    i = z[i][1]
    t += 1
z1.reverse()
print(t)
print(*z1)
