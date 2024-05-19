#WRONG ANSWER
n = int(input())
lista = []
for inputs in range(n*6):
    lista.append(list(map(int,input().split())))

regioes = [0, 0, 0, 0, 0]
nomes = ['superior', 'esquerda', 'centro', 'direita', 'inferior']
aux = 0

for i in range(n):
    if sum(lista[aux]) == 3:
        regioes[0] += 1
    else:
        soma = 0
        for a in range(1, 5):
            soma += lista[a][0]
        if soma == 4:
            regioes[1] += 1
        else:
            somaEsq, somaCen, somaDir = 0, 0, 0
            for a in range(1, 5):
                somaEsq += lista[a+aux][0]
                somaCen += lista[a+aux][1]
                somaDir += lista[a+aux][2]
            
            if(somaEsq == 4): 
                regioes[1] += 1
            
            elif(somaCen == 4):
                regioes[2] += 1
            
            elif(somaDir == 4):
                regioes[3] += 1

            elif sum(lista[aux+5]) == 3:
                regioes[4] += 1

    aux += 6

maximo = max(regioes)
print(nomes[regioes.index(maximo)])