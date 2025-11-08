a = int(input())
b = int(input())
s = 0
k = 0
for i in range (1,a-1):
    if a % i == 0 and b % i == 0:
        s = s + 1
for i in range (1,a-1):
    if a % i == 0 and b % i == 0:
        k = k + 1
        if k == s:
            print(i)
            exit()
   
