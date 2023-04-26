from hund import Hund


# Her testes hund.py
def hovedprogram():
    # Oppretter et objekt
    fido = Hund(5, 28)

    # Modifiserer objektet og sjekker ny verdi. Vekt bør ha økt med 1 etter definisjon i spis()
    fido.spring()
    fido.spis(1)
    fido.hentVekt()

    fido.spring()
    fido.spis(1)
    fido.hentVekt()


hovedprogram()
