def peresechenye_otrezkov(x1,y1,x2,y2,x3,y3,x4,y4):
    a12 = y2-y1
    b12 = x1-x2
    c12 = -x1 * a12 -y1 *b12
    a34 = y4-y3
    b34 = x3-x4
    c34 = -x3 * a34 -y3 *b34

    v1 = a34 *x1 + b34*y1 +c34
    v2 = a34 *x2 + b34*y2 +c34
    v3 = a12 *x3 + b12*y3 +c12
    v4 = a12 *x4 + b12*y4 +c12

    if ((v1 >= 0 and v2 <= 0) or (v1 <= 0 and v2 >= 0)) and ((v3 >= 0 and v4 <= 0) or (v3 <= 0 and v4 >= 0)):
        return True
    else:
        return False

s1 = 0
s = 0
q = []    
n =  int(input())
for i in range(n):
    q.append(list((map(int,input().split()))))

for i in range(0,n-1):
    for j in range(i+1,n):
        if peresechenye_otrezkov(q[i][0],q[i][1],q[i][2],q[i][3],q[j][0],q[j][1],q[j][2],q[j][3]):
            s += 1
    print(s)
    if s == 0:
        s1 += 1
    s = 0

print(s1)