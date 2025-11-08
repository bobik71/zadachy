a,b,c,d = map(int,input().split())
q = a + b + c +d
if q % 100 >= 11 and q % 100 <= 19:
    print(q, 'птиц')
elif q % 10 == 1:
    print(q, 'птица')
elif q % 10 >= 5 and q % 10 <= 9 or q % 10 == 0:
    print(q, 'птиц')
elif q % 10 >= 2 and q % 10 <= 4:
    print(q, 'птицы')
    