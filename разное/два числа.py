a, b = map(int,input().split())
for x in range(-1000000,1000000):
    y = (1 - a * x) // b
    if (1 - a * x) % b == 0:
        print(x,y)
        exit()
print(0,0)