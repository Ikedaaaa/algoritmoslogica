qj = int(input())
jogadores = []
pontos = []
for jogador in range(qj):
    jogadores.append(input())
    pontos.append(0)

rodadas = int(input())

for rodada in range(rodadas):
    palitos = list(map(int, input().split()))
    palpites = list(map(int, input().split()))
    somatoria = sum(palitos)
    for idx, palpite in enumerate(palpites):
        if palpite == somatoria:
            pontos[idx] += 1

vencedor = max(pontos)
print('EMPATE' if pontos.count(vencedor) > 1 else f"{jogadores[pontos.index(vencedor)]} GANHOU")