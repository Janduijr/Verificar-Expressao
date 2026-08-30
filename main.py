def verifica(x):
    global invalido
    if x == ')':
        if len(list) > 0:
            if '(' == list[-1]:
                del list[-1]
            else:
                invalido = True  
        else:
            invalido = True
    elif x == ']':
        if len(list) > 0:
            if '[' == list[-1]:
                del list[-1]
            else:
                invalido = True 
        else:
            invalido = True
    elif x == '}':
        if len(list) > 0:
            if '{' == list[-1]:
                del list[-1]
            else:
                invalido = True 
        else:
            invalido = True
    
a = '(a + b), {[a * (b + c)]}, a + {b - [c * d]}'
list = []
invalido = False

for x in a:
    if x in ['{','[','(']:
        list.append(x)
    
    verifica(x)
    

if invalido is False:
    if len(list) != 0:    
        print('NAO ESTA BALANCEADO!')
        print(f'FALTOU FECHAR OS SEGUINTES TERMOS: {list}')
    else:
        print('ESTA BALANCEADO!')
else:
    print('NAO ESTA BALANCEADO!')
    print('VOCE FECHOU ALGO QUE NAO ESTAVA ABERTO!')



