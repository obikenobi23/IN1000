class Celle:

    # Konstruktør
    def __init__(self):
        self.levende = bool()
        self.børleve = bool()
        pass

    # Endre status
    def settDoed(self):
        self.levende = False
        pass

    def settLevende(self):
        self.levende = True
        pass

    # Hente status
    def erLevende(self):
        if self.levende:
            return True
        else:
            return False
        pass

    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:
            return "."
        pass
