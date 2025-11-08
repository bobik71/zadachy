x1, y1 = (map(int,input().split()))
x2, y2 = (map(int,input().split()))
x3, y3 = (map(int,input().split()))
x4, y4 = (map(int,input().split()))

k1 = max(x1,x2)
k2 = min(x3,x4)
k3 = min(x1,x2)
k4 = max(x3,x4)

if k1 > k2 or k3 < k4:
    print('пересекатся')
else:
    print('непересекаются')