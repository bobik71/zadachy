def yb(n):
    if n < 1:
        return 
    else:
        print(n)
        yb(n-1)
n = int(input())

yb(n)