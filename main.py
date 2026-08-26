a = '(a + b), {[a * (b + c)]}, a + {b - [c * d]}'
list = []

for x in a:
    if x in ['{','}','(',')','[',']']:
        list.insert(0, x)

print(list)