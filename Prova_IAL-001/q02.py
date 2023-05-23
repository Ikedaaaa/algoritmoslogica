print("Caio Liang")
print("Matheus Marques Ikeda")
print("Questão 2")
print("\n**********************************************************\n")

def valorIsInLista(valor, lista):
    for item in lista:
        if item == valor:
            return True
    return False

LMin = int(input("Digite o menor valor inteiro de uma faixa de valores (maior que 0): "))
while LMin <= 0:
    print("\nÉ OBRIGATÓRIO QUE O MENOR VALOR SEJA MAIOR QUE 0!")
    LMin = int(input("Digite o menor valor inteiro de uma faixa de valores (maior que 0): "))

LMax = int(input("Digite o maior valor inteiro de uma faixa de valores: "))
while LMax <= LMin:
    print("\nÉ OBRIGATÓRIO QUE O MAIOR VALOR SEJA MAIOR QUE O MENOR VALOR!")
    LMax = int(input("Digite o maior valor inteiro de uma faixa de valores: "))
    
X = int(input("Digite um número inteiro diferente de 0: "))
while X == 0:
    print("\nÉ OBRIGATÓRIO O NÚMERO SER DIFERENTE DE 0!")
    X = int(input("Digite um número inteiro diferente de 0: "))
    
listaValores = []
somaValores = 0
print("\n\nDigite valores para serem inseridos em uma lista de acordo com três requisitos:")
print(f"1. Estar dentro da faixa {LMin} - {LMax}")
print(f"2. Ser divisível por {X}")
print(f"3. Não digitar números repetidos")
valor = int(input("\nDigite um valor inteiro (digite 0 para sair): "))
while valor != 0:
    if LMin <= valor <= LMax:
        if valor % X == 0:
            if not valorIsInLista(valor, listaValores):
                listaValores.append(valor)
            else:
                print(f"ATENÇÃO: {valor} já foi inserido na lista!")
        else:
            print(f"ATENÇÃO: O valor precisa ser divisível por {X}!")
    else:
        print(f"ATENÇÃO: {valor} está fora do intervalo {LMin} <= X <= {LMax}!")
    
    valor = int(input("\nDigite um valor inteiro (digite 0 para sair): "))
    
print("\n\n************************** VOCÊ ESCOLHEU SAIR! **************************")

print("\nOs elementos da lista são:")
for elemento in listaValores:
    print(elemento)
    
print(f"\nAo todo, a lista contém {len(listaValores)} elementos")

for elemento in listaValores:
    somaValores += elemento
print(f"Soma dos valores da lista: {somaValores}")

print(f"Média dos valores da lista: {somaValores / len(listaValores)}")

print("\n\n********************************** FIM DO PROGRAMA **********************************")