x = int(input())
for i in range(1,int(x**0.5)+2):
    if i ** 2 > x:
        print((i-1)**2)
        
