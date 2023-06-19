print("Projeto: Cálculo de Salários\n")
print("Integrantes:")
print("Caio Liang")
print("Matheus Marques Ikeda")
print("\n**********************************************************\n")

def getAliquotaINSS(salario):
    if salario <= 1751.81:
        return 0.08
    elif salario <= 2919.72:
        return 0.09
    elif salario <= 5839.45:
        return 0.11
    else:
        return 0
        
def getAliquotaEValorIR(salarioDescontado):
    if salarioDescontado <= 1903.98:
        return 0, 0
    elif salarioDescontado <= 2826.65:
        return 0.075, 142.8
    elif salarioDescontado <= 3751.05:
        return 0.15, 354.8
    elif salarioDescontado <= 4664.68:
        return 0.225, 636.13
    else:
        return 0.275, 869.36

salariosBrutos = []
maxLenSalario = 0

print("Lendo Arquivo de Salários")
with open("SALARIO.TXT", "r") as arquivoSalarios:
    salario = arquivoSalarios.readline().rstrip()
    while salario != "":
        #Coloquei o try/except pois a primeira linha do caso de teste 1 é "Bruto", o que dá erro ao converter para float
        try:
            salariosBrutos.append(float(salario))
            if len(salario) > maxLenSalario:
                maxLenSalario = len(salario)
            salario = arquivoSalarios.readline().rstrip()
        except:
            salario = arquivoSalarios.readline().rstrip()

print("Leitura de Arquivos Finalizada\n")

if maxLenSalario < 7:
    maxLenSalario = 7

columnsAlignedHeader = "{:>"+str(maxLenSalario)+"}{:>10}{:>11}{:>"+str((2 if maxLenSalario > 8 else 4)+maxLenSalario)+"}{:>8}{:>"+str(2+maxLenSalario)+"}{:>"+str(3+maxLenSalario)+"}\n"
columnsAlignedRows = "{:>"+str(maxLenSalario)+".2f}{:>10.1f}{:>11.2f}{:>"+str((2 if maxLenSalario > 8 else 4)+maxLenSalario)+".2f}{:>8.1f}{:>"+str(2+maxLenSalario)+".2f}{:>"+str(3+maxLenSalario)+".2f}\n"

print("Gravando arquivo de salários calculados")
with open("CALCULOS.TXT", "w") as arquivoCalculos:
    arquivoCalculos.write(columnsAlignedHeader.format("Bruto", "AliqINSS", "Val.INSS", "Base I.R.", "AliqIR", "Val.IR", "Liquido"))
    for salarioBruto in salariosBrutos:
        AliqINSS = getAliquotaINSS(salarioBruto)
        ValINSS = (salarioBruto * AliqINSS) if AliqINSS > 0 else 642.34
        BaseIR = salarioBruto - ValINSS
        AliqIR, DeducaoIR = getAliquotaEValorIR(BaseIR)
        ValIR = (BaseIR * AliqIR - DeducaoIR) if (DeducaoIR > 0 and AliqIR > 0) else 0
        if ValIR < 10:
            ValIR = 0
        salarioLiquido = salarioBruto - ValINSS - ValIR
        arquivoCalculos.write(columnsAlignedRows.format(salarioBruto, (AliqINSS*100), ValINSS, BaseIR, (AliqIR*100), ValIR, salarioLiquido))

print("Gravação de arquivo de salários calculados finalizada. Procure o arquivo CALCULOS.TXT\n")

print("******************** Fim do Programa ********************")
