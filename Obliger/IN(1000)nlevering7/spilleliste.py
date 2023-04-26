from sang import *

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn


    # Deloppgave 2.1
    def lesFraFil(self, filnavn):
        f = open(filnavn, "r")

        # Sangene legges til i en liste, og knyttes til artist i en ordbok.
        for linje in f:
            linje = linje.strip().split(";")
            nySang = Sang(linje[1],linje[0])
            self._sanger.append(nySang)
        print("Filen er hentet. Dette er slik spillelisten", self._navn, "ser ut nå:", self._sanger)
        f.close()

    # Deloppgave 2.2
    def leggTilSang(self, nySang):

        # Sangene legges til i en liste, og knyttes til artist i en ordbok.
        self._sanger.append(nySang)
        print("Dette er slik spillelisten", self._navn, "ser ut nå:", self._sanger)

    # Deloppgave 2.3
    def fjernSang(self, sang):

        # Teller gjennom sanglisten, og fjerner alle eventuelle treff både fra sanglisten og fra ordboken
        self._sanger.remove(sang)
        print("Sangen", sang, "er fjernet. Dette er slik spillelisten", self._navn, "ser ut nå:")
        #for i in self._sanger:
        #    print(i) # Denne kan fjernes
        return sang

    # Deloppgave 2.4
    def spillSang(self, sang):
        sang.spill()

    # Deloppgave 2.5
    def spillAlle(self):
        for i in self._sanger:
            print(i)
        return self._sanger

    # Deloppgave 2.6
    def finnSang(self, tittel):
        for i in self._sanger:
            if i.sjekkTittel(tittel):
                print("Sangen {} er i listen.".format(tittel))
                return i
        return None

    def hentArtistUtvalg(self, artistnavn):
        artistUtvalg = []

        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                artistUtvalg.append(i)

        """for i in self._sanger
            key = self._sanger[i]
            artistBiter = self._sangOrdbok[key].split(" ")  # Dette er en liste der hvert ord i artistens navn er et element
            if artistnavn in artistBiter:
                artistUtvalg.append(self._sanger[i])
                #artistUtvalg.append(self)"""
        return artistUtvalg




# Dette er diverse kommandoer som demonstrerer programmets funksjoner.
# Hvis programmet kjøres akkurat som det er, vil musikk.txt hentes og legges til i en spilleliste.
# Å fjerne kommentartegnene under vil gjøre andre fancy ting.
# Så er det bare å prøve seg fram :)
S1 = Spilleliste("Groovy funk")
S1.lesFraFil("musikk.txt")
print(S1._sanger)
#S1.spillAlle()
#print("Dette er sangene til Queen:", S1.hentArtistUtvalg("Queen"))
#S1.artistListe()