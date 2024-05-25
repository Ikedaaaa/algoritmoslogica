valor_carrinho, produtos_nao_carrinho = tuple(map(int, input().split()))
falta_para_frete_gratis = 200 - valor_carrinho
lista_produtos = []
frete_gratis = False

for x in range(produtos_nao_carrinho):
    lista_produtos.append(int(input()))

for a in range(len(lista_produtos)-2):
    for b in range(a+1, len(lista_produtos)-1):
        for c in range(b+1, len(lista_produtos)):
            d = (lista_produtos[a] + lista_produtos[b] + lista_produtos[c])
            if d == falta_para_frete_gratis:
                frete_gratis = True
                print(f"fretegratis")
                break
        if frete_gratis:
            break
    if frete_gratis:
        break

if not frete_gratis:
    print("fretepago")