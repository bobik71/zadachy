s = input()
for i in range(len(s)):
    s2 = s[:i] + s[i+1:]
    print(s2)