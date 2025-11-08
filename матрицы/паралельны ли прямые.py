x1, y1 = (map(int,input().split()))
x2, y2 = (map(int,input().split()))
x3, y3 = (map(int,input().split()))
x4, y4 = (map(int,input().split()))

a12 = y2-y1
b12 = x1-x2
c12 = -x1 * a12 -y1 *b12
a34 = y4-y3
b34 = x3-x4
c34 = -x3 * a34 -y3 *b34

if b12 == 0 and b34 == 0:
    print('паралельны')
elif b12 == 0 or b34 == 0:
    print('neпаралельны')
elif a12 / b12 == a34 / b34:
    print('паралельны')
else:
    print('neпаралельны')