import random

qtnMatriculas = int(input("Quantidade de matrículas a serem geradas: "))
with open('MATR.TXT', 'w') as f:
    for i in range(qtnMatriculas):
        newMatricula = ""
        for j in range(6):
            newMatricula += str(random.randint(0, 9))
        f.write(newMatricula + "\n")

