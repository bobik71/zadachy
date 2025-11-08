a2=list(map(str,input().split()))
a = [0,1,2,3]

while a[0] == 0:    
    for i in range(1,len(a)):
        print(a2[a[i]-1], end=' ')
    print()
    k = len(a) - 1
    while a[k-1] > a[k]:
        k -= 1
    i = len(a) - 1
    while a[i] < a[k-1]:
        i -= 1
    a[i], a[k-1] = a[k-1], a[i]
    a1 = a[:k]
    for i in range(len(a)-1, k-1, -1):
        a1.append(a[i])
    a = a1