class Hund:

    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hentAlder(self):
        print(self._alder)

    def hentVekt(self):
        print(self._vekt)

    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self, mat):
        self._metthet += mat
        if self._metthet > 7:
            self._vekt += 1
