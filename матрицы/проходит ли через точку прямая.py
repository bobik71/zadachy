x, y = (map(int,input().split()))
x4, y4 = (map(int,input().split()))
x1 = -1
y1 = -2
x2 = 2
y2 = 4
a = y2-y1
b = x1-x2
c = -x1 * a -y1 *b
v4 = a *x4 + b*y4 +c
v = a *x + b*y +c
if v4 == 0 and v == 0:
    print('обе лежат на прямой')
elif (v4 > 0 and v > 0) or (v4 < 0 and v < 0):
    print('лежат по одну сторону от прямой')
elif v4 == 0 and v != 0:
    print('одна лежит одна не лежит')
elif (v4 > 0 and v < 0) or (v4 < 0 and v > 0):
    print('лежат по разные стороны')