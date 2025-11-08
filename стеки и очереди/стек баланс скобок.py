a = input()
a1 = []
for i in a:
    if i == '(' or i == '[' or i == '{':
        a1.append(i)
    if i == ')' or i == ']' or i == '}':
        if len(a1) == 0:
            print('no')
            exit()
        else:
            k = a1[len(a1)-1]
            if k == '(' and i == ')':
                a1.pop()
            if k == '[' and i == ']':
                a1.pop()
            if k == '{' and i == '}':
                a1.pop()
if len(a1) == 0:
    print('yes')
else:
    print('no')

            

        
    


    