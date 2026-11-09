tijd = float(input("Hoeveel seconden telde je tussen de bliksem en de donder?: "))

afstand = round(tijd*343/1000 , 2)

if afstand >= 3:
    print(f"Je bent {afstand}km van het onweer verwijderd.")
    print("Je bent veilig!")

if afstand < 3:
    print(f"Je bent {afstand}km van het onweer verwijderd.")
    print("Ga plat op de grond liggen!")