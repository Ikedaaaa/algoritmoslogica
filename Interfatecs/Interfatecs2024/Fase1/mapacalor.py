#MAYBE RIGHT ANSWER
n = int(input())
pts = [0, 0, 0, 0, 0]
reg = ["superior", "esquerda", "centro", "direita", "inferior"]
aux = 0
matriz = []
for i in range(n*6):
	matriz.append([int(x) for x in input().split()])

for tela in range(n):
	if(sum(matriz[aux]) == 3):
		pts[0] += 1

	sumE, sumC, sumD = 0, 0, 0
	for i in range(1,5):
		sumE += matriz[i+aux][0]
		sumC += matriz[i+aux][1]
		sumD += matriz[i+aux][2]
	
	if(sumE == 4): 
		pts[1] += 1
	if(sumC == 4): 
		pts[2] += 1
	if(sumD == 4): 
		pts[3] += 1
	
	if(sum(matriz[aux+5]) == 3):
		pts[4] += 1
	aux += 6

#print(pts)
maximo = max(pts)
print(reg[pts.index(maximo)])