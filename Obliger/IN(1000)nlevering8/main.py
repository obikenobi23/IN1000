from spillebrett import Spillebrett
import random
def main():
    koordinat1 = input("Bestem brettets høyde (antall celler)")
    koordinat2 = input("Bestem brettets bredde (antall celler)")
    spill1 = Spillebrett(int(koordinat1),int(koordinat2))
    spill1.tegnBrett()

    while True:
        spillinput = input("Skriv inn \"Enter\" for å starte neste generasjon. \nSkriv \"q\" for å avslutte\n")
        if spillinput == "":
            spill1.oppdatering()
            spill1.tegnBrett()
        if spillinput == "q":
            break

# starte hovedprogrammet
main()