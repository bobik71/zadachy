q1, q2, q3, q4 = map(int,input().split())
s = q1 + q2 + q3 + q4
a = s % 10
v = s % 100
if a == 1:
    print(s, 'птица')
elif a == 5 or a == 0 or a == 6 or a == 7 or a == 8 or a == 9 or v == 11 or v == 12 or v == 13 or v == 14:
    print(s, 'птиц')
elif a == 2 or a == 3 or a == 4:
    print(s, 'птицы')
        


