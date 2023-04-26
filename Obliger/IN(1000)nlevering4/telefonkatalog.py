# Oppgave 5
# Oppgavetekst: Lag et program som lar brukeren legge til kontakter i en telefonkatalog. Den skal kunne knytte sammen navn og telefonnumre.

katalog = {"Erik Mohr Skorgan": "92828777",
           "Tafir Eilertsen": "46787154"
           }  # Katalogen har noen elementer fra før, så man kan lett teste uten å skrive inn et langt input selv.


def legg_til_i_katalog():
    navn = input("Skriv inn navnet til personen. ")
    tlf = input("Skriv inn telefonnummeret du vil knytte til kontakten. ")
    katalog[navn] = tlf  # De to verdiene assossieres som nøkkel og verdi i katalogen. Et navn kan assossieres med flere telefonnumre, men ikke motsatt.


løkke_liste = [""]

for i in løkke_liste:  # Løkken vil kjøre så lenge man legger til elementer i listen. Løkken starter funksjonen på nytt. Hvis man gir et tomt input, vil listen ikke bli lenger, og løkken vil slutte å kjøre.
    kjør_løkke = input(
        "Vil du legge til et navn i telefonkatalogen? (Hvis ja, skriv hva som helst og så trykk \"Enter\". Hvis ikke, bare trykk \"Enter\". ")
    løkke_liste.append(kjør_løkke)
    if (len(kjør_løkke) < 1):
        break
    legg_til_i_katalog()

print("Dette er navnene i telefonkatalogen din:")
print(katalog)

for j in katalog:
    print(j + ":")
    print(katalog[j])
