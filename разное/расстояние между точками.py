def r(x1,x2,y1,y2):
    c2 = ((x1-x2)**2+(y1-y2)**2)**0.5
    return(c2)
s =[]
k = 1000
t = 0
t1 = 0
n = int(input())
for i in range(n):
    s.append(list(map(int,input().split())))
for i in range(0,n-1):
    for j in range(i+1,n):
        if k > r(s[i][0],s[j][0],s[i][1],s[j][1]):
            k = r(s[i][0],s[j][0],s[i][1],s[j][1])
            t = i
            t1 = j
print(k,t+1,t1+1)