entrada = input().split()
entrada[0] = int(entrada[0])

for line in range(entrada[0]):
    letras = ""
    firstChar = 65 if entrada[1] == "maiusculas" else 97
    i = firstChar
    while i < firstChar + (line + 1):
        letras += chr(i)
        i += 1
    pontos = "." * (26 - len(letras))
    print(pontos + letras)
