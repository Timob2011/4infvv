getal1 = float(input("Hoeveel punten behaalde je?: "))
getal2 = float(input("Wat was de maximaal te behalen score?: "))

procent = (getal1/getal2)*100 

if procent >= 50:
    print(f"Proficiat, je bent geslaagd!")

if procent < 50: 
    print(f"Jammer, je bent niet geslaagd.")