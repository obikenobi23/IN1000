# Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
# og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
# instansvariabel hobbyer initialisert som en tom liste. Skriv en metode leggTilHobby
# som tar imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
# skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre. Gi deretter
# Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på
# metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
# med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så
# mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
# informasjon om brukeren skrives ut.

class Person:

    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self.hobbyer = []

    def leggTilHobby(self, nyHobby=""):
        self.hobbyer.append(nyHobby)

    def skrivHobbyer(self):
        print(f"{self._navn} liker: ", self.hobbyer)

    def skrivUt(self):
        print(self._navn, self._alder)
        self.skrivHobbyer()


Per = Person("Per", 75)
Per.leggTilHobby("skating")
Per.skrivUt()

nyttNavn = input("Hva skal den nye personen hete? ")
nyAlder = int(input(f"Hva er {nyttNavn} sin alder? "))
nyttNavn = Person(nyttNavn, nyAlder)

i = True
while i:
    nyHobby = input("Vil du legge til en hobby? (0 = nei) ")
    if nyHobby == "0":
        nyttNavn.skrivHobbyer()
        i = False
    else:
        nyttNavn.hobbyer.append(nyHobby)

# Siden det ikke lå noen føringer i oppgaveteksten valgte jeg å implementere hovedprogram() på den mest barbariske
# måten jeg kunne tenke meg. Jeg nevner dette slik at du som river deg i håret vet at jeg gjorde det med vilje.
