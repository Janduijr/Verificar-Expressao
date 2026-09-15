# Verificador de Balanceamento de Parênteses, Colchetes e Chaves

Programa em Python que verifica se uma expressão possui parênteses `()`, colchetes `[]` e chaves `{}` corretamente balanceados, utilizando uma pilha (lista) para controlar a abertura e o fechamento de cada símbolo.

## Como funciona

O programa percorre a string caractere por caractere:

- Quando encontra um símbolo de **abertura** (`(`, `[`, `{`), ele é adicionado à pilha.
- Quando encontra um símbolo de **fechamento** (`)`, `]`, `}`), o programa verifica se o topo da pilha corresponde à abertura esperada:
  - Se corresponder, remove o símbolo da pilha (fechamento válido).
  - Se não corresponder ou a pilha estiver vazia, a expressão é marcada como **inválida**.

Ao final, o programa avalia dois cenários:

1. Se algum fechamento não teve abertura correspondente → `NAO ESTA BALANCEADO!` (fechou algo que não estava aberto).
2. Se sobrou algum símbolo na pilha sem fechamento → `NAO ESTA BALANCEADO!` (falta fechar termos, exibindo quais).
3. Se a pilha ficar vazia e nenhum erro ocorrer → `ESTA BALANCEADO!`.

## Exemplo de entrada

```python
a = '(a + b), {[a * (b + c)]}, a + {b - [c * d]}'
```

## Exemplo de saída

```
ESTA BALANCEADO!
```

## Como usar

1. Edite a variável `a` no código com a expressão que deseja testar.
2. Rode o script:
   ```
   python verifica.py
   ```
3. O resultado será exibido no terminal.
