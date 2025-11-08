a = input()
z = {}
for i in a:
    if i in z:
        z[i] += 1
    else:
        z[i] = 1
for i in range(ord('a'),ord('z')+1):
    if chr(i) in z:
        print(chr(i),'-',z[chr(i)])
    else:
        print(chr(i),'-',0)
