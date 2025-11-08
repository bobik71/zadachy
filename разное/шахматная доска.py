n, m = map(int, input().split())
if n % 2==0 and m%2==0:
    print(n*m//2)
elif n % 2 ==1 and m % 2 == 0:
    print((m* n)//2)
elif n % 2 == 0 and m % 2 == 1:
    print(n // 2 * m)
elif n % 2 == 1 and m%2== 1:
    print((n//2+1)*m-m // 2)