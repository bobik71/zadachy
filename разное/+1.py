a = map(int,input().split())
a = list(a)
f = len(a)
max = a[0]
min = a[0]
for i in range(f):
    if a[i] > max:
        num = i
        max = a[i]
    if a[i] < min:
        n = i
        min = a[i]
a[num] = min
a[n] = max
print(a)
            
        
        
