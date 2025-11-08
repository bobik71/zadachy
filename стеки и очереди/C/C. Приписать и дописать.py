w = int(input())
for i in range(w):
    g = int(input())
    s1 = input()
    ss = list(s1)
    s = len(ss)
    while (ss[0] == '1' and ss[len(ss)-1] == '0') or (ss[0] == '0' and ss[len(ss)-1] == '1'):
        s -= 2
        ss.pop()
        ss.pop(0)
    print(s)

