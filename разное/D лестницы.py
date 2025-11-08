n = int(input())
a = map(int, input().split())
a = list(a)
m = 1
c = 1
for i in range(1, n):
    if a[i] > a[i - 1]: 
        c = c + 1
    else:  
        if c > m:
            m = c
        c = 1  
if c > m:
    m = c
print(m)
