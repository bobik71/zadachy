def fiba(n):
    a = 0
    b = 1
    c = [0]*100
    c[0]=a
    c[1]=b
    for i in range(2,n+1):
        c[i] = c[i-1] + c[i-2]
    return(c[n-1])

def r(k):
    n = 1
    while k != fiba(n):
        n += 1
        if k < n:
            return('NO')
    return('YES',n)


k = int(input())

print(r(k))