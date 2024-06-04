def format_input(param):
    inscricao_categorias = []
    for categoria in range(1, len(param)):
        inscricao_categorias.append(int(param[categoria]))

    return param[0], inscricao_categorias
    
vagas = int(input())
inscritos_categorias = [
    [], #ALGORITMOS
    [], #BOAS PRATICAS
    [], #DESEMPENHO
    [], #FLUXOGRAMAS
    [], #INTERPRETACAO DE ENUNCIADOS
    [], #SINTAXE DE LINGUAGEM
    []  #FICA PARA A PROXIMA
]

inscritos = 0

entrada = input()
while entrada != '':
    inscritos += 1
    if inscritos <= 5:
        nome, categorias = format_input(entrada.split())
        for categoria in categorias:
            if len(inscritos_categorias[categoria-1]) < vagas:
                inscritos_categorias[categoria-1].append(nome)
            else:
                inscritos_categorias[6].append(nome)

    entrada = input()

for categoria in range(0, len(inscritos_categorias)-1):
    inscritos_categorias[categoria].sort()
    print('------------------------------')
    if categoria == 0:
        print('ALGORITMOS')
    elif categoria == 1:
        print('BOAS PRATICAS')
    elif categoria == 2:
        print('DESEMPENHO')
    elif categoria == 3:
        print('FLUXOGRAMAS')
    elif categoria == 4:
        print('INTERPRETACAO DE ENUNCIADOS')
    else:
        print('SINTAXE DA LINGUAGEM')
    print('------------------------------')

    for inscrito in inscritos_categorias[categoria]:
        print(inscrito)
    
    if categoria < 5:
        print()

if len(inscritos_categorias[6]) > 0:
    print('\n------------------------------')
    print('FICA PARA A PROXIMA!')
    print('------------------------------')
    for inscrito in inscritos_categorias[6]:
        print(inscrito)