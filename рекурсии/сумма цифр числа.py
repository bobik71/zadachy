def sch(n):
    if n == 0:
        return 0
    else:
        l= n % 10
        return l + sch(n // 10)
    
n = int(input())

print(sch(n))