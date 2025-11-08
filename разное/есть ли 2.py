a = map(int,input().split())
a = list(a)
k = len(a)
s = 0
for i in range(k):
    if a[i] == 2:
        s = s + 1
if s != 0:
    print('есть')
else:
    print('нету')
