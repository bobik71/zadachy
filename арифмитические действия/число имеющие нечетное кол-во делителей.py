t = int(input())
for j in range(t):
    n = int(input())
    for i in range(n,1,-1):
        if i**0.5 == int(i**0.5):
            print(i)
            break