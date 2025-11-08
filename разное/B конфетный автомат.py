a, b, c, d = map(int,input().split())
if (a + b) % 2 == 0:
    x = (a + b) // 2
else:
    x = a + b

if (c + d) % 2 == 0:
    y = (c + d) // 2
else:
    y = c + d
if (x + y) % 2 == 0:
    candies = (x + y) // 2
else:
    candies = x + y
print(candies)


