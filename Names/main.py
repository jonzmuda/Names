import random

Gender_Input = input("Specify Gender:")
if Gender_Input == "Girls":
    with open("girls.txt",'r') as g:
        for line in g:
            girls = line.split()
            print(random.choice(girls))
elif Gender_Input == "Boys":
    with open("boys.txt",'r') as b:
        for line in b:
            boys = line.split()
            print(random.choice(boys))
    