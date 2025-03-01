str = input()
output = []

for i in str :
    if i.islower() == True :
        print(i.upper(), end="")
    else :
        print(i.lower(), end="")

