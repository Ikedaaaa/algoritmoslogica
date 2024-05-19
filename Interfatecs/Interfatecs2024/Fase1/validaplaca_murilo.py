placa = str(input())
asci = ord(placa[0])
qtnd = len(placa)
numerica = 0
cont = 0
cont3 = 3
cont4 = 4
cont5 = 5


if(qtnd > 7):
    print("Placa inválida")
else:
    for digit in placa:
        if(48 <= asci <= 57):
            if(48 <= ord(digit) <= 57):   
                numerica += 1
                if(numerica == qtnd):
                   print("Placa numerica")
                   break
        elif (65<= asci <= 90):
            if(48 <= ord(placa[1]) <= 57) and placa[0] in 'AP':
                #print(asci)
                if(48 <= ord(placa[cont]) <= 57):
                    cont += 1
                    if(cont == qtnd):
                        print("Placa muito antiga")
                        break
            else:
                if(48 <= ord(placa[2]) <= 57):
                    if(48 <= ord(placa[cont3]) <= 57):
                        cont3 += 1
                        if(cont3 == qtnd):
                            print("Placa AA-9999")
                            break
                elif 48 <= ord(placa[3]) <= 57:
                    if(48 <= ord(placa[cont4]) <= 57):
                        cont4 += 1
                        if(cont4 == qtnd):
                            print("Placa AAA-9999")
                            break
                    elif 65<= ord(placa[4]) <= 90:
                        if(48 <= ord(placa[cont5]) <= 57):
                            cont5 += 1
                            if cont5 == qtnd:
                                print("Placa Mercosul")
                                break
                    else:
                        print("Placa invalida")
                        break
                else:
                    print("Placa invalida")
                    break
        else:
            print("Placa invalida")
            break

