from random import randrange
computer = randrange(5)+1

gok = int(input("Waag een gokje! Raad een getal tussen 1 en 5: "))

if gok == computer:
    print("Proficiat, je hebt het getal geraden!")

if gok != computer:
    print(f"Fout, het juiste getal was {computer}.")
