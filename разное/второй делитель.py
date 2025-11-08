a = int(input())
s = 0
for i in range (a,0,-1):
    if a % i == 0:
        s = s + 1
    if s == 2:
        print(i)
        exit()
