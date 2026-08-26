class pilha:
    def push(list):
        if len(list) < 5:
            a = input('digite algo: ')
            list.insert(0, a)
        else:
            print('a lista esta cheia!')

    def pop(list):
        print(f'removi o item da posicao {0}:', list[0])
        del list[0]

    def top(list):
        print('Desempilhando')
        print(f'posicao {0}:', list[0])

    def vazia(list):
        if len(list) == 0:
            print('a lista esta vazia!')
        elif len(list) > 5:
            print('a lista esta cheia!')

p1 = pilha()
p1.push(1,2,3)






    
