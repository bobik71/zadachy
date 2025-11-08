
def pvg(q):
   print(q)
   z[q] = 1
   for i in range(1,n+1):

       if z[i] == 1 and i != q:
            for j in range(len(p)):
                if p[j] == i:
                    r = j
            if ((len(p)-1)-r) == 2:
               print('YES')
               exit()
       if s[q][i] == 1 and z[i] == 0:
           p.append(i)
           pvg(i)
           
           
        
p = []
r = 0
n = int(input())
a1 = [0]*(n+1)
s1 = [0]*(n+1)
s = []
f = list(map(int,input().split()))
for i in range(n+1):
    s.append(s1.copy())
for i in range(1,n+1):
    s[i][f[i-1]] = 1
for i in range(n+1):
    print(s[i])
z  =[0]*(n+1)
pvg(1)