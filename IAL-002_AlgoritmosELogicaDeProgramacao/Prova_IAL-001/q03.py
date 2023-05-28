print("Caio Liang")
print("Matheus Marques Ikeda")
print("Questão 3")
print("\n**********************************************************\n")

def findProductById(Id, listaProdutos):
    for produto in listaProdutos:
        if produto[0] == Id:
            return True, produto
    return False, []

totalVendasVarejo = 0
totalVendasAtacado = 0

produtos = []
produtos.append([16, 14.35, 12.93, 50])
produtos.append([23, 35.12, 29.85, 100])
produtos.append([27, 19.35, 16.76, 70])
produtos.append([34, 63.40, 58.25, 40])

NV = int(input("Digite o número de vendas: "))
while NV <= 0:
    print("NÚMERO DE VENDAS PRECISA SER MAIOR QUE 0!")
    NV = int(input("Digite o número de vendas: "))

print(f"\n\nDigite {NV} vendas da seguinte forma:\nX Y\nX representa o código do produto\nY representa a quantidade de venda")
print("Deve haver um espaço em branco entre X e Y!\n")

for i in range(NV):
    Cod, QV = tuple(map(int, input("Informe a venda: ").split()))
    productWasFound, produto = findProductById(Cod, produtos)
    
    if productWasFound:
        if QV < produto[3]:
            totalVendasVarejo += (QV * produto[1])
        else:
            totalVendasAtacado += (QV * produto[2])
    else:
        print("Código inválido")
        
print()
print("Total de Vendas do Grupo Varejo: R$", "{:.2f}".format(totalVendasVarejo))
print("Total de Vendas do Grupo Atacado: R$", "{:.2f}".format(totalVendasAtacado))
print("\nVendas Totais: R$", "{:.2f}".format(totalVendasVarejo + totalVendasAtacado))