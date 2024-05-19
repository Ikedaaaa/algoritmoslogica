placa = input()

antiga = False
numerica = False
placa_aa = False
placa_aaa = False
mercosul = False

def change_values(a, b, c, d, e):
    global antiga, numerica, placa_aa, placa_aaa, mercosul
    antiga, numerica, placa_aa, placa_aaa, mercosul = a, b, c, d, e

if len(placa) <= 7:
    for caracter in range(len(placa)):
        ascii_valor = ord(placa[caracter])
        if 65 <= ascii_valor <= 90:
            if caracter == 0:
                change_values(True if placa[caracter] in ['A', 'P'] else False, False, True, True, True)
            elif caracter == 1:
                change_values(False, False, True, True, True)
            elif caracter == 2:
                change_values(False, False, False, True, True)
            elif caracter == 4:
                change_values(False, False, False, False, True)
            else:
                change_values(False, False, False, False, False)
                break
        else:
            if caracter == 0:
                change_values(False, True, False, False, False)
            elif caracter == 1:
                change_values(True, True, False, False, False)
            elif caracter == 2:
                change_values(True, True, True, False, False)
            elif caracter == 3:
                change_values(True, True, True, True, True)
            elif caracter == 4:
                change_values(True, True, True, True, False)
            elif caracter == 5:
                change_values(True, True, True, False if mercosul else True, False if placa_aaa else True)
            elif caracter == 6:
                change_values(False, True, False, False if mercosul else True, False if placa_aaa else True)

if mercosul:
    print("Placa Mercosul")
elif placa_aaa:
    print("Placa AAA-9999")
elif placa_aa:
    print("Placa AA-9999")
elif numerica:
    print("Placa numerica")
elif antiga:
    print("Placa muito antiga")
else:
    print("Placa invalida")
print(antiga, numerica, placa_aa, placa_aaa, mercosul)