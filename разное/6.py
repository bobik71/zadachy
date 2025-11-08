a = int(input())
b = int(input())
w = 0
for i in range(a,0,-1):
    if a % i == 0 and b % i == 0:
        w = w + 1
        if w == 2:
            print(i)
            exit()
       
