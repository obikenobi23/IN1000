class Dato:

    def __init__(self, nyDag, nyMåned, nyttÅr):
        self._dag = nyDag
        self._måned = nyMåned
        self._år = nyttÅr

    # Deloppgave 2.a
    def hentÅr(self):
        print(self._år)

    # Deloppgave 2.b
    def visDato(self):
        print(self._dag, "/", self._måned, "/", self._år)

    # Deloppgave 2.c
    def erSamme(self, dag, måned):
        if self._måned == måned:
            if self._dag == dag:
                print("Det er samme dato som dagen i systemet.")
            else:
                print("Det er ikke samme dato som den du oppga.")
        else:
            print("Det er ikke samme dato som den du oppga.")

    # Deloppgave 2.d
    def sammenliknDato(self, dag, måned, år):

        # Sammenlikner år
        if self._år < år:
            print("Datoen er større enn den lagrede datoen.")
        elif self._år > år:
            print("Den lagrede datoen er større enn den du skrev inn.")
        elif self._år == år:

            #Hvis årene er like sammenliknes måned
            if self._måned < måned:
                print("Datoen er større enn den lagrede datoen.")
            elif self._måned > måned:
                print("Den lagrede datoen er større enn den du skrev inn.")
            elif self._måned == måned:

                # Hvis månedene er like sammenliknes dato
                if self._dag < dag:
                    print("Datoen er større enn den lagrede datoen.")
                elif self._dag > dag:
                    print("Den lagrede datoen er større enn den du skrev inn.")
                else:
                    print("Datoene er like.")

    # Deloppgave 2.e
    def iMorgen(self):
        # Datoskifte
        self._dag += 1

        ## Månedskifte
        # Vanlige måneder
        if self._måned == 1 or self._måned == 3 or self._måned == 5 or self._måned == 7 or self._måned == 8 or self._måned == 10 or self._måned == 12:
            if self._dag > 31:
                self._dag = 0
                self._måned += 1
        elif self._måned == 4 or self._måned == 6 or self._måned == 9 or self._måned == 11:
            if self._dag > 30:
                self._dag = 0
                self._måned += 1

        # Februar
        elif self._måned == 2:

            # Skuddår
            if (self._år % 4 == 0 or self._år % 400 == 0) and self._år % 100 != 0:
                if self._dag > 29:
                    self._dag = 0
                    self._måned += 1

            # Vanlig februar
            elif self._dag > 28:
                self._dag = 0
                self._måned += 1
            else:
                print("Skuddårsfeil")
        else:
            print("Månedparameter er galt")
            return

        # Årsskifte
        if self._måned > 12:
            self._måned = 1
            self._år += 1
