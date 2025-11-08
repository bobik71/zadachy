def abr(s):
    if len(s) > 10:
        print(s[0]+str(len(s)-2)+s[len(s)-1])
    else:
        print(s)

q = []
n = int(input())

for i in range(n):
    s = input()
    q.append(s)

for i in range(n):
    if abr(q[i]) != None:
        print(abr(q[i]))