d1, d2 = map(int,input().split())
s = 0
for i in [1,2,3,4,5,6]:
    if i >= d1 and i >= d2:
        s+=1
n6 = 6
if s%2 == 0:
    s //= 2
    n6 //= 2
if s%3==0:
    s //= 3
    n6 //= 3
print(s,'/',n6, sep = '')