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
        return f"Linha {lineNumber} – Venda cancelada"
    elif errorCode == 190:
        return f"Linha {lineNumber} – Venda não finalizada"
    elif errorCode == 999:
        return f"Linha {lineNumber} – Erro desconhecido. Acionar equipe de TI."
    else:
        return f"Linha {lineNumber} – Código de Produto não encontrado {productId}"

produtos = []
vendas = []
transferencias = []
divergencias = []
totcanais = [["1 - Representantes", 0], ["2 - Website", 0], ["3 - App móvel Android", 0], ["4 - App móvel iPhone", 0]]

with open('PRODUTOS.TXT', 'r') as arquivoProdutos:
    infoProduto = arquivoProdutos.readline().rstrip()
    while infoProduto != "":
        infoProdutoAsList = formatFileLine(infoProduto)
        produtos.append(infoProdutoAsList)
        transferencias.append([infoProdutoAsList[0], 0, infoProdutoAsList[1], 0, 0])
        infoProduto = arquivoProdutos.readline().rstrip()

with open('VENDAS.TXT', 'r') as arquivoVendas:
    infoVenda = arquivoVendas.readline().rstrip()
    while infoVenda != "":
        vendas.append(formatFileLine(infoVenda))
        infoVenda = arquivoVendas.readline().rstrip()

#************* PROCESSAMENTO DOS DADOS DE ENTRADA **************
for idx, venda in enumerate(vendas):
    productIdx = getProductIdxById(venda[0])

    if productIdx > -1:
        if venda[2] in [100, 102]:
        else:
            divergencias.append(getDivergency(venda[2], idx+1, 0))
    else:
        divergencias.append(getDivergency(404, idx+1, venda[0])) #Error 404 - Not Found
