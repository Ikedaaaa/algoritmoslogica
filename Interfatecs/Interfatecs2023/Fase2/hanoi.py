discos = int(input())
tot = (2**discos-1)
inpt = input().split()
dec = 0
i = 0
j = len(inpt)-1
while(j>=0):
    if(inpt[j] == '1'):
        dec += pow(2, i)
    i+=1
    j-=1
print(tot-dec)
