import random
from celle import Celle


class Spillebrett:
    # Konstruktør
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._brett = []
        self._generasjon = 0
        self._generer()
        pass

    def tegnBrett(self):

        # "Rens" skjermen før brettet tegnes
        print("----------------")

        # Tegner brettet
        for i in self._brett:
            for j in i:
                print(j.hentStatusTegn(), end="")
            print()

        # Gi metainfo om gjeldende generasjon
        print("Generasjon", self._generasjon)
        print("Antall levende celler: ",self.finnAntallLevende())
        print("Høyde: {} Bredde: {}".format(self._rader, self._kolonner))
        print("----------------")
        pass

    # Les brettet
    def oppdatering(self):
        self._generasjon += 1

        # Del cellene inn etter hvorvidt de skal overleve eller bli levende, eller dø eller forbli døde
        børLeve = []
        børDø = []

        # Let rundt cellen etter naboer, legg dem til i listen over naboer
        for rad in self._brett:
            for celle in rad:
                levendeNaboer = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        siderad = self._brett.index(rad) + i
                        sidekolonne = rad.index(celle) + j

                        # Utelukk tilfeller der siderad eller sidekolonne ikke finnes
                        if siderad < 0 or siderad >= self._rader:
                            continue
                        elif sidekolonne < 0 or sidekolonne >= self._kolonner:
                            continue
                        elif i == 0 and j == 0:
                            continue
                        else: # Tell opp antall levende naboer
                            if self._brett[siderad][sidekolonne].erLevende():
                                levendeNaboer.append(self._brett[siderad][sidekolonne])

                            for k in range(-1, 2): # Inkludér diagonaler
                                if sidekolonne + k in self._brett[siderad]:
                                    diagonal = self._brett[siderad][sidekolonne + k]
                                    if self._brett[siderad][diagonal].erLevende():
                                        levendeNaboer.append(self._brett[siderad][diagonal])

                # Bruk reglene i Game of Life til å bestemme om cellen skal leve eller dø
                if celle.erLevende():
                    if len(levendeNaboer) in range(2, 4):
                        børLeve.append(celle)
                    else:
                        børDø.append(celle)
                else:
                    if len(levendeNaboer) == 3:
                        børLeve.append(celle)
                    else:
                        børDø.append(celle)

        # Bugtest, inklusivt hvilken celle det er noe galt med
        feilmelding = 0
        teller = 0
        for rad in self._brett:
            for celle in rad:
                if celle in børLeve:
                    teller += 1
                    celle.settLevende()
                elif celle in børDø:
                    teller += 1
                    celle.settDoed()
                else:
                    print("Her gikk noe galt:", celle)
                    feilmelding += 1
                    teller += 1
                    print("Antall feilmeldinger:",feilmelding)
                    print("Cellenr:",teller)

    def finnAntallLevende(self):
        # finnAntallLevende skal gjøre nøyaktig det det leses som:
        # Finne hvor mange som lever
        antallLevende = 0
        for i in self._brett:
            for j in i:
                if j.erLevende():
                    antallLevende += 1
        return antallLevende

    def _generer(self):
        # Legger til rader som lister i listen. Kolonnene legges til som celler.
        for i in range(self._rader):
            self._brett.append([])
            for j in range(self._kolonner):
                self._brett[i].append(Celle())

        # Gir cellene verdi "levende" eller "død" før spillet starter
        for i in range(self._rader):
            for j in range(self._kolonner):
                liv_diceRoll = random.randrange(0, 3)  # Tilfeldig tall fra 0 til 2: sannsynlighet på 1/3
                if liv_diceRoll == 2:
                    self._brett[i][j].settLevende()
                else:
                    self._brett[i][j].settDoed()
        pass

    def finnNabo(self, rad, kolonne):

        pass
