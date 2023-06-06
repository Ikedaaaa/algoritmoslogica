L, C, B = tuple(map(int, input().split()))

X, Y = tuple(map(int, input().split()))

movimentos = [*input()]

parede = 0

movimento = 0
while movimento < B and movimento < len(movimentos):
    if movimentos[movimento] == "C":
        if X == 1:
            parede += 1
        else:
            X -= 1
    elif movimentos[movimento] == "B":
        if X == L:
            parede += 1
        else:
            X += 1
    elif movimentos[movimento] == "D":
        if Y == C:
            parede += 1
        else:
            Y += 1
    else:
        if Y == 1:
            parede += 1
        else:
            Y -= 1
    movimento += 1

print("{} {} {}".format(X, Y, parede))
