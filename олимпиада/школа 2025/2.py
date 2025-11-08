n, k = map(int,input().split())
s = input()
i = 0
f = 0

while i < n:
    if s[i] == 'F':
        i += k
        f += 1
    else:
        i += 1

print(f)