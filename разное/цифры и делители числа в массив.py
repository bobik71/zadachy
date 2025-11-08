a = int(input())
g = []
o = []
for i in range(1,a):
    if a % i == 0:
        g.append(i)
while a > 0:
    k = a % 10
    a = a // 10
    o.append(k)
print(g, o)
      
     
