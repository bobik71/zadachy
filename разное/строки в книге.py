k, n = map(int, input().split())
if k >= n:
    print(1,n)
elif k<n and n-n//k*k == 0:
    print(n//k,k)
elif k<n and n-n//k*k != 0:
    print(n//k+1,n-n//k*k)