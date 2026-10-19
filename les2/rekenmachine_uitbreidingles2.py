getal1 = float(input("geef getal 1: ")) #float maakt het een kommagetal
getal2 = float(input("geef getal 2: "))
bewerking = input("Welke bewerking wil je uitvoeren? (+,-,/,*,m): ")

if bewerking == "+":  #== : is gelijk aan ; <= : kleiner dan en gelijk aan ; < : kleiner dan ; != niet gelijk aan
    print(f"{getal1} + {getal2} = {getal1+getal2}.")

if bewerking == "-":
    print(f"{getal1} - {getal2} = {getal1-getal2}.")

if bewerking == "/":
    print(f"{getal1} / {getal2} = {getal1/getal2}.")

if bewerking == "*":
    print(f"{getal1} * {getal2} = {getal1*getal2}.")

if bewerking == "m":
    print(f"{getal1} ** {getal2} = {getal1**getal2}.")