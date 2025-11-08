def rast(s1,s2):
    s = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s += 1
    return s

n ,m = map(int,input().split())
a = []
s = 0
for i in range(n):
    a.append(input())
for i in range(0,n-1):
    for j in range(i+1,n):
        s = s + rast(a[i],a[j])

print(s)
