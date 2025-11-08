def st(a,b):
    if b == 1:
        return(a)
    else:
        return a * st(a,b-1)
    
a = int(input())
b = int(input())

print(st(a,b))