n = int(input())
primo = 2
for i in range(2, n):
    if n > 4 and n % 2 == 0:
        break
    if n % i == 0:
        primo += 1
        if primo > 3:
            break

print('sim' if primo == 3 else 'nao')