a = 'a + (b, {[a * b], (a + b)}, a + {b - [c * d}'
list = []
abre = 0
fecha = 0

for x in a:
    if x in ['}',')',']']:
        fecha += 1
        list.insert(0, x)

for x in a:
    if x in ['{','(','[']:
        abre += 1
        list.insert(0, x)

print(list)
if abre == fecha:
    print('TUDO OK!')
else:
    print('NAO ESTA BALANCEADO!')