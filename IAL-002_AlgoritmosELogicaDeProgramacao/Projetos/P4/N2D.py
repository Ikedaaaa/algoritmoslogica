print("Projeto: Estoque Operacional\n")
print("Integrantes:")
print("Caio Liang")
print("Matheus Marques Ikeda")
print("\n**********************************************************\n")

def formatFileLine(line):
    return list(map(int, line.split(';')))

def getProductIdxById(Id):
    for idx, produto in enumerate(produtos):
        if produto[0] == Id:
            return idx
    return -1

def getDivergency(errorCode, lineNumber, productId):
    if errorCode == 135:
        return f"Linha {lineNumber} - Venda cancelada"
    elif errorCode == 190:
        return f"Linha {lineNumber} - Venda não finalizada"
    elif errorCode == 999:
        return f"Linha {lineNumber} - Erro desconhecido. Acionar equipe de TI"
    else:
        return f"Linha {lineNumber} - Código de Produto não encontrado {productId}"

produtos = []
vendas = []
transferencias = []
divergencias = []
totcanais = [["1 - Representantes", 0], ["2 - Website", 0], ["3 - App móvel Android", 0], ["4 - App móvel iPhone", 0]]

#******************* ENTRADA DE DADOS ********************
print("Lendo arquivo PRODUTOS.TXT")
with open('PRODUTOS.TXT', 'r') as arquivoProdutos:
    infoProduto = arquivoProdutos.readline().rstrip()
    while infoProduto != "":
        infoProdutoAsList = formatFileLine(infoProduto)
        produtos.append(infoProdutoAsList)
        transferencias.append([infoProdutoAsList[0], 0, infoProdutoAsList[1], 0, 0])
        infoProduto = arquivoProdutos.readline().rstrip()

print("Lendo arquivo VENDAS.TXT")
with open('VENDAS.TXT', 'r') as arquivoVendas:
    infoVenda = arquivoVendas.readline().rstrip()
    while infoVenda != "":
        vendas.append(formatFileLine(infoVenda))
        infoVenda = arquivoVendas.readline().rstrip()

#************* PROCESSAMENTO DOS DADOS DE ENTRADA **************

print("\nProcessando os dados de entrada\n")
for idx, venda in enumerate(vendas):
    productIdx = getProductIdxById(venda[0])

    if productIdx > -1:
        if venda[2] in [100, 102]:
            transferencias[productIdx][1] += venda[1] #QtVendas
            transferencias[productIdx][2] -= venda[1] #Estoq.após
            totcanais[venda[3]-1][1] += venda[1] #QtVendas por canal
        else:
            divergencias.append(getDivergency(venda[2], idx+1, 0))
    else:
        divergencias.append(getDivergency(404, idx+1, venda[0])) #Error 404 - Not Found

i = 0
while i < len(transferencias):
    if transferencias[i][2] < produtos[i][2]:
        transferencias[i][3] = produtos[i][2] - transferencias[i][2] #Necessidade
        
    transferencias[i][4] = 10 if 1 < transferencias[i][3] < 10 else transferencias[i][3] #Transf. de Arm p/ CO
    i += 1

#*********** GRAVAÇÃO DOS DADOS NOS DEVIDOS ARQUIVOS ************

print("Gravando informações no arquivo TRANSFERE.TXT\n")

arqTransfLineFmt = "{:<7}{:>6}{:>7}{:>10}{:>11}{:>9}{:>12}\n"
with open("TRANSFERE.TXT", "w") as arquivoTransferencias:
    arquivoTransferencias.write("Necessidade de Transferência Armazém para CO\n\n")
    arquivoTransferencias.write(arqTransfLineFmt.format("Produto", "QtCO", "QtMin", "QtVendas", "Estq.após", "Necess.", "Transf. de"))
    arquivoTransferencias.write(arqTransfLineFmt.format("", "", "", "", "Vendas", "", "Arm p/ CO"))

    for idx, transferencia in enumerate(transferencias):
        arquivoTransferencias.write(arqTransfLineFmt.format(transferencia[0], produtos[idx][1], produtos[idx][2], transferencia[1], transferencia[2], transferencia[3], transferencia[4]))

print("Gravando informações no arquivo DIVERGENCIAS.TXT\n")
with open("DIVERGENCIAS.TXT", "w") as arquivoDivergencias:
    for divergencia in divergencias:
        arquivoDivergencias.write(divergencia+"\n")

print("Gravando informações no arquivo TOTCANAIS.TXT\n")
with open("TOTCANAIS.TXT", "w") as arquivoTotcanais:
    arquivoTotcanais.write("Quantidades de Vendas por canal\n\n")
    arquivoTotcanais.write("{:<23}{:>8}\n".format("Canal", "QtVendas"))

    for totcanal in totcanais:
        arquivoTotcanais.write("{:<23}{:>8}\n".format(totcanal[0], totcanal[1]))

print("******************** Fim do Programa ********************")
