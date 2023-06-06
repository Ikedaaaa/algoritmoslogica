import re
senha = input()
flag = True
if bool(re.search('[a-z]+',senha)) and bool(re.search('[A-Z]+',senha)) and bool(re.search('[0-9]+',senha)) and bool(re.match('^[a-zA-Z0-9]*$',senha)) and 6 <= len(senha) <= 15:
    i = 0
    while i < len(senha)-1 and flag:
        if ord(senha[i]) + 1 == ord(senha[i+1]):
            flag = False
        i += 1
    print(str(flag))
else:
    print("False")
