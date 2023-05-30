print("Projeto: Totalização simples de vendas de produtos\n")
print("Integrantes:")
print("Caio Liang")
print("Matheus Marques Ikeda")
print("\n**********************************************************\n")

totalQtnVendas = 0
totalProdutos = 0
totalVendas = 0
vendas = []

def formatSaleItem(string):
    global totalProdutos, totalVendas
    #Para a formatação da linha, é removido o \n e cada item separado por ";" é jogado em uma lista
    linha = string.strip().split(";")

    qtnProduto = int(linha[1])
    precoProduto = float(linha[2])

    #Já começa a contabilizar o total geral e o total de produtos vendidos
    totalProdutos += qtnProduto
    totalVendas += (qtnProduto * precoProduto)

    #Retorna cada item como [int, int, float]
    return [int(linha[0]), qtnProduto, precoProduto]

def sortByProductId(idx):
    return idx[0]

def binarySearch(valueToFind, isUniqueValue):
    menorIdxBusca = 0
    maiorIdxBusca = len(vendas)
    meioBusca = getIntervalHalfIdx(menorIdxBusca, maiorIdxBusca)
    menorIdxValueToFind = -1
    idxsSearched = []
    
    while meioBusca not in idxsSearched:
        idxsSearched.append(meioBusca)
        if vendas[meioBusca][0] == valueToFind:
            #Se os valores fossem únicos, poderia retornar direto
            #Como há duplicados, tenta encontrar o menor idx com o valor
            if isUniqueValue:
                return meioBusca
            else:
                menorIdxValueToFind = meioBusca
                maiorIdxBusca = meioBusca
                meioBusca = getIntervalHalfIdx(menorIdxBusca, maiorIdxBusca)
        else:
            if valueToFind > vendas[meioBusca][0]:
                menorIdxBusca = meioBusca
                meioBusca = getIntervalHalfIdx(menorIdxBusca, maiorIdxBusca)
            else:
                maiorIdxBusca = meioBusca
                meioBusca = getIntervalHalfIdx(menorIdxBusca, maiorIdxBusca)
    
    if menorIdxValueToFind > -1:
        return menorIdxValueToFind
    else:
        return -1

def getIntervalHalfIdx(lowestValue, highestValue):
    intervalSize = highestValue - lowestValue
    return lowestValue + (intervalSize // 2)

print("Lendo arquivo...")

with open("vendas.txt", "r") as file:
    #O arquivo é lido linha por linha com o file.readline()
    #Cada linha é formatada e jogada numa lista
    line = file.readline()
    while line != "":
        vendas.append(formatSaleItem(line))
        line = file.readline()
        
    totalQtnVendas = len(vendas)

print("Leitura de arquivo finalizada\n")

print("Total de vendas:", totalQtnVendas)
print("Total de produtos vendidos:", totalProdutos)
print("Total em vendas: R$", "%.2f" % totalVendas)
print()

vendas.sort(key=sortByProductId)

codigo = int(input("Digite o código: "))
while codigo != 0:
    if 10000 <= codigo <= 21000:
        totalVendidoProduto = 0
        codigoIdx = binarySearch(codigo, False)
        
        if codigoIdx > -1:
            while codigoIdx < len(vendas) and vendas[codigoIdx][0] == codigo:
                totalVendidoProduto += (vendas[codigoIdx][1] * vendas[codigoIdx][2])
                codigoIdx += 1

        print("Total vendido do produto", codigo, "= R$", "%.2f" % totalVendidoProduto)
    else:
        print(codigo, "Código inválido (deve ser entre 10000 e 21000)")
                
    codigo = int(input("\nDigite o código: "))

print("Fim do programa")
