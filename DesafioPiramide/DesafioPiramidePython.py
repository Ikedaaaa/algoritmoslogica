print("********************** PIRÂMIDE DE LADO N **********************")
print("Ao digitar um número N, o programa irá imprimir uma pirâmide de base quadrada de lado N * N, como se fosse vista de cima")
print("Cada nível da pirâmide deve ser representado pelo número correspondente ao \"andar\" de cada nível")
print("Exemplo:\ninput: 4\nSaída:\n1 1 1 1\n1 2 2 1\n1 2 2 1\n1 1 1 1")
print("\ninput: 5\nSaída:\n1 1 1 1 1\n1 2 2 2 1\n1 2 3 2 1\n1 2 2 2 1\n1 1 1 1 1")
print("\n***********************************************************************************\n")
qtnLado = int(input("Digite um número N representando o tamanho do lado de uma pirâmide: "))
meioPiramide = qtnLado / 2

for i in range(qtnLado):
    nivel = 1
    linha = '1'
    for j in range(qtnLado - 1):
        if i < meioPiramide:
            if j + 1 < meioPiramide and nivel < i + 1:
                nivel += 1
            elif nivel > 1 and j >= qtnLado - (i + 1):
                nivel -= 1
        else:
            if j + 1 < meioPiramide and nivel < qtnLado - i:
                nivel += 1
            elif nivel > 1 and j >= (qtnLado - (qtnLado - i)):
                nivel -= 1
        linha += ' ' + str(nivel)
            
    print(linha)
