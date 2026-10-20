from random import randrange

getal1 = randrange(100)+1
getal2 = randrange(100)+1

antwoord = int(input(f"{getal1} + {getal2} = "))

som = getal1+getal2

if antwoord == som:
    print("Je hebt de som juist")

if antwoord != som:
    print(f"Fout, het juiste antwoord was {som}")