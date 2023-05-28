print("Caio Liang")
print("Matheus Marques Ikeda")
print("Questão 1")
print("\n**********************************************************\n")

segundosInput = int(input("Digite a quantidade de segundos consumidos para realizar a tarefa: "))
horas = 0
minutos = 0
segundos = 0

if segundosInput > 0:
    horas = segundosInput // 3600
    segundosInput -= (horas * 3600)

if segundosInput >= 60:
    minutos = segundosInput // 60
    segundosInput -= (minutos * 60)

if segundosInput > 0:
    segundos = segundosInput
    
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")