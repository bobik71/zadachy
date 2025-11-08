def rpvg(q):
    b[q] = 1
    for i in range(1, n + 1):
        if s[q][i] == 1 and b[i] == 0:  
            rpvg(i)  

n = int(input()) 
b = [0] * (n+1)  
m = int(input())  
s1 = [0]*(n+1)
s = []
for i in range(n+1):
    s.append(s1.copy())

for i in range(m):
    a, x = map(int, input().split())
    s[a][x] = 1
    s[x][a] = 1  

g = 0  
for i in range(1,n+1):  
    if b[i] == 0:  
        rpvg(i)  
        g += 1  

print(g)
