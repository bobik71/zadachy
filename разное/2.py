q1 = int(input())
q2 = int(input())
q3 = int(input())
q4 = int(input())
s = q1 + q2 + q3 + q4
if s == 1:
    print('1 птица')
if s == 2 or 3 or 4:
    print(s,'птицы')
else:
    print(s, ' птиц')
