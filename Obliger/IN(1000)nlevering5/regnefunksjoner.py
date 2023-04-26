def addisjon(tall1, tall2):
    return tall1 + tall2

print(addisjon(5, 8))


def substraksjon(tall1, tall2):
    return tall1 - tall2

assert substraksjon(7, 2) == 5
assert substraksjon(-4, -11) == 7
assert substraksjon(15, -4) == 19


def divisjon(tall1, tall2):
    return tall1 / tall2

assert divisjon(7, 6) > 1
assert divisjon(-13, -7) < 2
assert divisjon(20, -5) == -4



def tommer_til_cm(antall_tommer):
    assert antall_tommer > 0
    antall_cm = antall_tommer * 2.54
    return antall_cm

print(tommer_til_cm(5))



def multiplikasjon(tall1, tall2): #Bruker må få lov til å multiplisere også
    return tall1 * tall2


def skriv_beregninger():
    tall_input1 = float(input("Skriv inn et tall "))
    tall_input2 = float(input("Skriv inn et annet tall "))
    operasjon_valg = int(input("Hva slags operasjon vil du utføre på tallene? 1 = addisjon, 2 = substraksjon, 3 = multiplikasjon, 4 = divisjon "))
    if operasjon_valg == 1:
        print(addisjon(tall_input1, tall_input2))
        print(tall_input1 + tall_input2)
    elif operasjon_valg == 2:
        print(substraksjon(tall_input1, tall_input2))
    elif operasjon_valg == 3:
        print(multiplikasjon(tall_input1, tall_input2))
    elif operasjon_valg == 4:
        print(divisjon(tall_input1, tall_input2))
    else:
        print("Det er ikke en gyldig input.")

    tommetall = float(input("Skriv inn et antall tommer. Du kan skrive et desimaltall. Bruk da . som komma. "))
    print(tommer_til_cm(tommetall))

skriv_beregninger()