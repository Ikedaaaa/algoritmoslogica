andares, N = tuple(map(int, input("(andares) Nº entre 1 e 100 | (Casos de teste) Nº entre 1 e 200 (separados por espaço em branco): ").split()))

while andares != 0 and N != 0:
    portas = "C" * andares
    for i in range(N):
        multiplo = int(input("Digite o múltiplo: "))
        idxString = multiplo
        while idxString <= andares:
            portas = portas[:idxString-1] + ("C" if portas[idxString-1] == "O" else "O") + portas[idxString:]
            idxString += multiplo
    print(portas)
    andares, N = tuple(map(int, input("(andares) Nº entre 1 e 100 | (Casos de teste) Nº entre 1 e 200 (separados por espaço em branco): ").split()))
