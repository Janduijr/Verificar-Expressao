a = ' (a + b), {[a * (b + c)]}, a + {b - [c * d]}'
list = []
invalido = False

for x in a:
    if x in ['{','[','(']:
        list.append(x)
    if x == ')':
        if len(list) > 0:
            if '(' == list[-1]:
                del list[-1]
            else:
                invalido = True  
                break
        else:
            invalido = True
            break
    elif x == ']':
        if len(list) > 0:
            if '[' == list[-1]:
                del list[-1]
            else:
                invalido = True 
                break
        else:
            invalido = True
            break
    elif x == '}':
        if len(list) > 0:
            if '{' == list[-1]:
                del list[-1]
            else:
                invalido = True 
                break
        else:
            invalido = True
            break

if invalido is False:
    if len(list) != 0:
        print('NAO ESTA BALANCEADO!')
    else:
        print('ESTA BALANCEADO!')
else:
    print('NAO ESTA BALANCEADO!')



