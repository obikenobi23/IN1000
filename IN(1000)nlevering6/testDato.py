from dato import Dato


def hovedprogram():
    # Deloppgave 3.a
    dag1 = Dato(15, 3, 2021)

    # Deloppgave 3.b
    dag1.hentÅr()

    # Deloppgave 3.c
    if dag1._dag == 15:
        print("Lønningsdag!")
    elif dag1._dag == 1:
        print("Ny måned, nye muligheter")

    # Deloppgave 3.d
    dag1_tekst = str(dag1.visDato())

    # Deloppgave 3.e
    print(dag1_tekst)

    # Deloppgave 3.f
    dag1.iMorgen()
    dag1.visDato()

    # Deloppgave 3.g
    nyDag = int(input("Skriv inn en dato som du vil sammenlikne med den i systemet. "))
    nyMåned = int(input("Skriv inn en måned. "))

    dag1.erSamme(nyDag, nyMåned)


hovedprogram()
