#Versão final
qntd = int(input())
while qntd != 0:
    resultado = ""
    spin = 1
    soma = 3
    while spin <= qntd:
        resultado += (str(spin) if resultado == "" else (" " + str(spin)))
        spin = spin + soma
        soma += 2
    print(resultado)
    qntd = int(input())

#Primeira Versão - Time Limit Exceeded
qntd = int(input())
quantumGates = [*("C"*qntd)]
while qntd != 0:
    resultado = ""
    multiplo = 1
    while multiplo <= qntd:
        i = multiplo - 1
        while i < qntd:
            quantumGates[i] = "C" if quantumGates[i] == "O" else "O"
            i += multiplo
        multiplo += 1
    for idx, quantumGate in enumerate(quantumGates):
        if quantumGate == "O":
            resultado += str(idx + 1) if resultado == "" else (" " + str(idx + 1))

    print(resultado)
    qntd = int(input())
    quantumGates = [*("C"*qntd)]
