def nod(a,b):
    while a != b:
        a, b = max(a,b) - min(a,b), min(a,b)   
        return a
    
a = int(input())
b = int(input())
print(nod(a,b))