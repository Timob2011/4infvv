getal1 = float(input("Hoeveel euro betaalde je voor je zonnepanelen? ")) 
premie = getal1 /100 * 20

if premie  <= 600:
    print(f"Je krijgt een premie van {premie} euro.")

if premie > 600:
    print(f"Je krijgt een premie van 600 euro.")