n = int(input())
k = int(input())
a = list(map(int,input().split()))
a1 = [0]*n

for i in range(k):
    t = a.index(min(a))
    a1[i] = min(a)
    a1[i] = a[t]
    a.pop(t)
for i in range(len(a)):
    if a1[i+k] == 0:
        a1[i+k] = a[i]    
print(a1)