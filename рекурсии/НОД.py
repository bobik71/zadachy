def nod(a,b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)
    
a = int(input())
b = int(input())
print(nod(a,b))