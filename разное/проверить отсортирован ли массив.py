n = int(input())
a = map(int,input().split())
a = list(a)
k = 0
for i in range(len(a)):
    if a[i] >= a[i+1]:
        k += 1
if k == len(a):
    exit()
k = 0

