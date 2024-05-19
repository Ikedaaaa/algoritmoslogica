'''
usu = input().split()
hsh = []
while(usu[0] != 'ACABOU'):
    tot = 0
    for idx, l in enumerate(usu[1]):
        tot += ord(l)*(idx+1)
        
    psw = str(tot)+
    hsh.append([usu[0], psw])
    usu = input().split()
for i in hsh:
    print(i)
'''
tot = 0
primosStr = "2"
num = 3
while num < 616100:
    isPrime = True
    i = 1
    while (i < num) and isPrime:
        if (num % i == 0) and  i not in [1, num]:
            isPrime = False
            
        i += 1
    if isPrime:
        primosStr += ", " + str(num)

    num += 1
    if num % 10000 == 0:
        print(num)
print(primosStr)
