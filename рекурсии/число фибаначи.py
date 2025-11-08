def fiba(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fiba(n-1) + fiba(n-2)

n = int(input())

print(fiba(n))