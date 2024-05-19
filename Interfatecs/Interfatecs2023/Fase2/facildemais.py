testes = int(input())
posPrimo = int(input())
par = True if posPrimo == 1 else False

for i in range(testes-1):
    posPrimo = int(input())

    if posPrimo != 1:
        par = not par

print("par" if par else "impar")
