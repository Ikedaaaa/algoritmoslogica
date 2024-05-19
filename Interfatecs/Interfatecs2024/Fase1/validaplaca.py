#FEITO NO METRÔ E BUSÃO, DEPOIS DO TÉRMINO DA COMPETIÇÃO, APÓS TER UM MOMENTO "EUREKA"
#(acredito que isso seja facilmente resolvido com RegEx)
placa = input()
t = len(placa)
if t == 1:
    if (48<=ord(placa[0])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 2:
    if (65<=ord(placa[0])<=90) and (placa[0] in 'AP') and (48<=ord(placa[1])<=57):
        print('Placa muito antiga')
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 3:
    if (65<=ord(placa[0])<=90) and (placa[0] in 'AP') and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57):
        print('Placa muito antiga')
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 4:
    if (65<=ord(placa[0])<=90) and (placa[0] in 'AP') and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57):
        print('Placa muito antiga')
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 5:
    if (65<=ord(placa[0])<=90) and (placa[0] in 'AP') and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57):
        print('Placa muito antiga')
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 6:
    if (65<=ord(placa[0])<=90) and (65<=ord(placa[1])<=90) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57) and (48<=ord(placa[5])<=57):
        print("Placa AA-9999")
    elif (65<=ord(placa[0])<=90) and (placa[0] in 'AP') and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57) and (48<=ord(placa[5])<=57):
        print('Placa muito antiga')
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57) and (48<=ord(placa[5])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
elif t == 7:
    if (65<=ord(placa[0])<=90) and (65<=ord(placa[1])<=90) and (65<=ord(placa[2])<=90) and (48<=ord(placa[3])<=57) and (65<=ord(placa[4])<=90) and (48<=ord(placa[5])<=57) and (48<=ord(placa[6])<=57):
        print("Placa Mercosul")
    elif (65<=ord(placa[0])<=90) and (65<=ord(placa[1])<=90) and (65<=ord(placa[2])<=90) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57) and (48<=ord(placa[5])<=57) and (48<=ord(placa[6])<=57):
        print("Placa AAA-9999")
    elif (48<=ord(placa[0])<=57) and (48<=ord(placa[1])<=57) and (48<=ord(placa[2])<=57) and (48<=ord(placa[3])<=57) and (48<=ord(placa[4])<=57) and (48<=ord(placa[5])<=57) and (48<=ord(placa[6])<=57):
        print("Placa numerica")
    else:
        print("Placa invalida")
else:
    print("Placa invalida")