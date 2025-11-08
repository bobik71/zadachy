n = int(input())
u = input()
sr = n // 2 
k = 0

if n % 2 == 0:
    print('NOT POSSIBLE')
    exit()


for i in range(n):
    ui = u[:i] + u[i+1:]
    s1 = ui[:sr]
    s2 = ui[sr:]
    if s1 == s2:
        k = k+1
        s3 = s2
if k == 1:
    print(s3)
elif k == 0:
    print('NOT POSSIBLE')
else:
    print('NOT UNIQUE')