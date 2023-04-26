class Motorsykkel:

    def __init__(self, merke, registreringsnummer, kjørelengde=0.0):
        self._merke = merke
        self._reg = registreringsnummer
        self._lengde = kjørelengde

    def kjør(self, lengde):
        self._lengde += lengde

    def hentKilometeravstand(self):
        return self._lengde

    def skrivUt(self):
        print(self._merke)
        print(self._reg)
        print(self._lengde)
