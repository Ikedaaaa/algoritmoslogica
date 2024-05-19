#WRONG ANSWER
testes = int(input())
pendencias = []
dependencias = []
for i in range(testes):
    teste = input().split()
    pendencias.append(teste[0])
    dependencias.append(teste[1])
ciclo = False
for idx, pendencia in enumerate(pendencias):
    cQ = False
    cP = False
    q = []
    p = []
    for i, dep in enumerate(dependencias):
        x = pendencias[idx]
        if(x in q): cQ = True
        if(pendencias[idx] in p): cP = True
        if(idx != i):
            pendencias[idx] = dependencias[idx]
            dependencias[idx] = x 
            q.append(x)
            p.append(pendencias[idx])
if(cQ and cP): ciclo = True
print("usar injecao tardia" if ciclo else "ok")
