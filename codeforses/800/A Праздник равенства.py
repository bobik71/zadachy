n = int(input())
a = list(map(int,input().split()))
s = 0
for i in a:
    s += max(a)-i
print(s)