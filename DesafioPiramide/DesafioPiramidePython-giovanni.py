import numpy as np

n = int(input())

# criando a piramide n X n
piramide = np.ones((n,n), dtype=int)

# percorrendo cada camada é adicionando 1
for i in range(1, (n+1)//2):
    piramide[i:n-i,i:n-i] += 1

print(piramide)
