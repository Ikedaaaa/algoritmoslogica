testes_candidatos = int(input())
saidas = []

for i in range(testes_candidatos):
    grad, spec, mestreArea, mestreNArea, tempo = tuple(map(int, input().split()))

    if (grad == 1 and (mestreNArea == 1 or mestreArea == 1)) or (mestreArea == 1):
        if tempo >= 3:
            saidas.append(f"Cand. {i+1}: deferido (comprovar 3 anos)")
        else:
            saidas.append(f"Cand. {i+1}: INDEFERIDO (exp)")
    elif grad == 1 and spec == 1:
        if tempo == 5:
            saidas.append(f"Cand. {i+1}: deferido (comprovar 5 anos)")
        else:
            saidas.append(f"Cand. {i+1}: INDEFERIDO (exp)")
    else:
        saidas.append(f"Cand. {i+1}: INDEFERIDO (acad)")

for saida in saidas:
    print(saida)
