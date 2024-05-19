n = int(input())

anagram = [
    'ABC',
    'DEF',
    'GHI',
    'JKL',
    'MNO',
    'PQRS',
    'TUV',
    'WXYZ'
]

for i in range(n):
    palavra = [*input()]
    saida = ''
    for letra in palavra:
        for idx, valor in enumerate(anagram):
            if letra in valor:
                saida += str(idx + 2)

    print(saida)