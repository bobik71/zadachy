def sort(q):
    rpvg(q)


def rpvg(q):
    b[q] = 1
    for i in range(1, n + 1):
        if b[i] == 0:  
            rpvg(i)  

n = int(input())
l = []
b = [0] * (n+1) 
s = [None]*n
for i in range(n):
    l.append(int(input()))
    if l[i] != -1:
        s[i] = l[i]

g = 0  
glav = []
for i in range(1,n+1):  
    if b[i] == 0:
        glav.append(b[i])
        rpvg(i)  
        g += 1  

for i in range(len(glav)):
    sort(glav[i])