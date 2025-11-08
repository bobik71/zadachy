a=list(map(int,input().split()))

while a[0] == 0:    
    print(a[1:])
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