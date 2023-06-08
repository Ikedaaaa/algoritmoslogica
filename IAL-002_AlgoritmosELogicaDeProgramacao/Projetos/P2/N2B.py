print("Projeto: Gerador de Senhas\n")
print("Integrantes:")
print("Caio Liang")
print("Matheus Marques Ikeda")
print("\n**********************************************************\n")

import random

matriculas = []

def getCharsSenha(pwdType):
    pwdCharacterTypes = []
    
    #Cada número de 0 a 3 representa um caracter que pode estar na senha, baseado no tipo da senha
    # Caso o tipo seja 'a', a lista terá apenas o valor [0], ou seja, apenas algarismos,
    # Se for 'b', terá [1, 2]
    # Se for 'c', terá [0, 1]
    # Se for 'd', terá [0, 1, 2]
    # Se for 'e', terá [0, 1, 2, 3]
    if pwdType in ['a', 'c', 'd', 'e']:
        pwdCharacterTypes.append(0) #algarismos
    if pwdType in ['b', 'c', 'd', 'e']:
        pwdCharacterTypes.append(1) #letras maiúsculas
    if pwdType in ['b', 'd', 'e']:
        pwdCharacterTypes.append(2) #letras minúsculas
    if pwdType in ['e']:
        pwdCharacterTypes.append(3) #caracteres especiais
    
    return pwdCharacterTypes

def GeraSenha(Tipo, Tam):
    senha = ""
    charsSenha = getCharsSenha(Tipo)
    specialChars = ["-", "_", ":", "@", "#", "$", "&", "?"]
    for char in range(Tam):
        randomIdxCharsSenha = random.randint(0, len(charsSenha)-1)
        
        #Com base nos tipos de valores possíveis para a senha definidos na lista charsSenha,
        #é escolhido um índice aleatório dessa lista para definir o próximo caracter da senha baseado no valor desse índice
        # Se charsSenha = [1, 2] e randomIdxCharsSenha = 1 -> charsSenha[randomIdxCharsSenha] = 2
        # Ou seja, pegará uma letra minúscula
        if charsSenha[randomIdxCharsSenha] == 0:
            senha += chr(random.randint(48, 57)) #algarismos
        elif charsSenha[randomIdxCharsSenha] == 1:
            senha += chr(random.randint(65, 90)) #letras maiúsculas
        elif charsSenha[randomIdxCharsSenha] == 2:
            senha += chr(random.randint(97, 122)) #letras minúsculas
        elif charsSenha[randomIdxCharsSenha] == 3:
            senha += specialChars[random.randint(0, len(specialChars)-1)] #caracteres especiais
            
    return senha

#************************* Input do usuário *************************
print("Qual é o tipo de senha que deve ser gerada?")
print("  a. Numérica – conterá apenas algarismos;")
print("  b. Alfabética – conterá apenas letras maiúsculas e minúsculas;")
print("  c. Alfanumérica 1 – conterá letras maiúsculas e algarismos;")
print("  d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;")
print("  e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres \"-\", \"_\", \":\", \"@\", \"#\", \"$\", \"&\", \"?\"")

tipoSenha = input("\nTipo da senha: ")
#Apesar de não ser solicitado, coloquei validação para o tipo da senha e para o seu tamanho não ser 0 ou negativo
while tipoSenha not in ['a', 'b', 'c', 'd', 'e']:
    print("\nATENÇÃO: Opção inválida. Digite novamente")
    tipoSenha = input()
    
tamanhoSenha = int(input("\nAgora digite o tamanho da senha, ou a quantidade de caracteres que a mesma deve conter: "))
while tamanhoSenha < 1:
    print("\nATENÇÃO: A senha não pode ter tamanho 0 ou negativo. Digite novamente")
    tamanhoSenha = int(input())

#******************** Leitura do Arquivo de Entrada ********************
print("\nLendo arquivo de entrada")
try:
    with open("MATR.TXT", "r") as file:
        line = file.readline()
        while line != "":
            matriculas.append(line.strip())
            line = file.readline()
except:
    print("Houve um problema ao ler o arquivo")
finally:
    print("Leitura de arquivo finalizada\n")

#******************** Gerando arquivo de senhas ********************
print("Gerando arquivo de senhas")
try:
    with open('SENHAS.TXT', 'w') as f:
        for matricula in matriculas:
            senha = GeraSenha(tipoSenha, tamanhoSenha)
            f.write(matricula + ";" + senha + ";\n")
except:
    print("Houve um problema ao escrever no arquivo de senhas")
finally:
    print("Arquivo de senhas gerado com sucesso\n")
    
print("************ Fim do Programa ************")
