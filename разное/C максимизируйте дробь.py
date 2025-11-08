n = int(input())
a = map(int,input().split())
a = list(a)
min1 = min(a)
max1 = max(a)
s = 0
def sort(k):
    for i in range(len(a)):
        if a[i] >= a[i+1]:
            k += 1
    if k == len(a):
        return 1
    else:
        return 0
for i in range(len(a)):
    for j in range(i,len(a)):
        c = a[i:j+1]
        c = list(c)
        if (max(c) == max1) and (min(c) == min1):
            s += 1
print(sort(s))
