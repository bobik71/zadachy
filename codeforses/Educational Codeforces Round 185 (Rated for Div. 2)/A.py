t = int(input())
for i in range(t):
    a = []
    n = int(input())
    for i in range(n):
        a.append([])
        for j in range(i*n+1,(n+i*n)+1):
            a[i].append(j)
    su = 0
    #for i in range(n):
        #for j in range(n):
            #if i == n and j == n-1:
                #su += a[i][j]
    if n == 2:
        su += a[n-1][n-1]
        su += a[n-2][n-1]
        su += a[n-1][n-2]
        print(su)

    elif n == 1:
        print(1)
    
    elif n <5:
        su += a[n-1][n-2]
        su += a[n-1][n-1]
        su += a[n-2][n-2]
        su += a[n-1][n-3]
        print(su)
    else:
        su += a[n-1][n-2]
        su += a[n-2][n-1]
        su += a[n-2][n-2]
        su += a[n-2][n-3]
        su += a[n-3][n-2]
        print(su)