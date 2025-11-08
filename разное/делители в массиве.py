a = []
s = 0
k = int(input())
for i in range(1,k):
    if k % i == 0:
        a.append(i)
l = len(a)
#for i in range(l):
    #s = s + a[i]
print(sum(a))
