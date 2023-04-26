class Sang:

    def __init__(self, artist, tittel):
        self._artist = str(artist)
        self._tittel = str(tittel)

    def __str__(self):
        return(f"\"{self._tittel}\" av {self._artist}")

    def spill(self):
        print(f"Spiller {self._tittel} av {self._artist}.")

    def sjekkArtist(self, navn):
        liste = navn.split(" ")

        for i in liste:
            artistListe = self._artist.split(" ")

            if i in artistListe:
                return True
        return False

    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

    def sjekkArtistOgTittel(self, navn, tittel):
        return self.sjekkArtist(navn) and self.sjekkTittel(tittel)

"""        self.navn = str(navn)
        liste = self.navn.split(" ")

        self.tittel = str(tittel)

        if self.tittel.lower() == self._tittel.lower():
            for i in liste:
                if i in self._artist:
                    return True
                else:
                    return False
        else:
            return False"""


#sang1 = Sang("Hozier", "Talk")
#sang2 = Sang("Marcy Playground", "Sex and Candy")

#print(sang2.spill())
#print(sang1.sjekkArtistOgTittel("Hozier", "Talk"))
#print(sang2.sjekkArtist("Playground"))
#print(sang2.sjekkArtistOgTittel("Marcy", "sex and candy"))
#print(sang2)
#print(sang1.spill())