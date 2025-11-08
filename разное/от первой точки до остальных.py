def r(x1,x2,y1,y2):
    c2 = ((x1-x2)**2+(y1-y2)**2)**0.5
    return(c2)
n = int(input())
s = 1000
a, b = (map(int,input().split()))
for i in range(0,n-1):
    a1, b1 = (map(int,input().split()))
    t = r(a,a1,b,b1)
    if t < s:
        s = t
        v = i
print(s,v)