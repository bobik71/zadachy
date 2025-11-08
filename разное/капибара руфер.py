n, k = map(int,input().split())
s = input()
s1 = ''
for i in s:
    if i <= '4' and k > 0:
        f = 9 - int(i)
        f = str(f)
        s1 += f
        k -= 1
    else:
        s1 += i
print(s1)
