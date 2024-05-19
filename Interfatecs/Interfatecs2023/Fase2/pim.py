pim = int(input())
string = "1"

for i in range(pim-1):
    string += " " + (str(i+2) if (i+2) % 4 != 0 else "pim")

print(string)