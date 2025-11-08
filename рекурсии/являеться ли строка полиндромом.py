def pol(s):
    if len(s) <= 1:
        #print('YES')
        return True
    else:
        if s[0] != s[-1]:
            #print('NO')
            return False
        pol(s[1:-1])  
         

s = input()
print(pol(s))
