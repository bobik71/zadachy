n = []
a = map (int,input().split())
a = list(a)
n = len(a)
x = a[0]
u = a[n-1]
a[0] = u
a[n-1] = x
print(a)
    
