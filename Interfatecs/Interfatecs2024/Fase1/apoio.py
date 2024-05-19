nPerfis = int(input())
minPorPerfil = list(map(int, input().split()))
nRegioes = int(input())

for nRegiao in range(nRegioes):
    reg = list(input().split())
    grupoMin = 0
    for i in range(nPerfis):
        if(i == 0):
            grupoMin = int(reg[i+1])//minPorPerfil[i]
        else :
            grupoMin = min(grupoMin, int(reg[i+1])//minPorPerfil[i])
    print(f"{reg[0]} {grupoMin}")