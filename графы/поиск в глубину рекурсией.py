def pvg(q):
   print(q)
   z[q] = 1
   for i in range(len(s[q])):
       if z[s[q][i]] == 0:
           pvg(s[q][i])
           
        

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
z  =[0]*(n+1)
pvg(1)