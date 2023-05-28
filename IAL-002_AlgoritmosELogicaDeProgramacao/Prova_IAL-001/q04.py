print("Caio Liang")
print("Matheus Marques Ikeda")
print("Questão 4")
print("\n**********************************************************\n")

N = int(input("Digite um número ímpar obedecendo ao intervalo 5 <= X <= 49: "))

if N % 2 != 0 and 5 <= N <= 49:
    arvore = []
    nivelArvore = ''
    tronco = ''
    base = ''
    
    for i in range(N):
        nivelArvore += '*'
    
    while len(nivelArvore) >= 1:
        arvore.append(nivelArvore)
        nivelArvore = nivelArvore[2:]
    
    for x in range(N // 2):
        tronco += " "
    tronco += "|"
    
    for x in range((N // 2) - 1):
        base += " "
    base += "---"
    
    i = len(arvore)
    while i > 0:
        saidaArvore = ''
        for espaco in range(i - 1):
            saidaArvore += " "
        saidaArvore += arvore[i - 1]
        print(saidaArvore)
        i -= 1
    
    print(tronco)
    print(base)
else:
    print(f"O número {N} é inválido")
