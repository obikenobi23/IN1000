#Dette er oppgave 1 i innleveringen
#Oppgave 1.2 - 1.3
print("Hei Student! Kan du si meg navnet ditt? ")
navn = input()
#Jeg foretrekker å gi input på egen linje, heller enn å skrive svaret inn på samme linje som spørsmålet.
navn = navn.lower()
navn = navn.capitalize()
#Disse to kommandoene sørger for at kun forbokstaven er stor, i tilfelle brukeren skrev feil.
print("Hei," , navn)

#Opgave 1.4
langtStrå = 5
kortStrå = 3
#Disse variablene definerer lengder. I "loren" er disse lengdene et kort og et langt strå.

print("Det lengste strået er", langtStrå, "cm langt.")
print("Det korteste strået er", kortStrå, "cm langt.")
#For meg som jobber med programmet er det en gardering å se mer enn to tall på hver sin linje i terminalen. Hvis koden skulle kjøre, men ikke virke helt som tiltenkt, er det enklere å se hvilken del av koden som har en "fungerende feil" hvis hver linje i output har litt kontekst.

#Oppgave 1.5
diff = abs(langtStrå - kortStrå)
#diff lagrer differansen på lengdene. abs() gir differansen i positivt fortegn, uansett hvilken rekkefølge tallene settes i.

print("Differanse:", diff)

#Oppgave 1.6
print("Hva er etternavnet på favorittskuespilleren din?")
fanNavn = input()
#Samme prosess som over, ber om et navn og legger det i en variabel.
fanNavn = fanNavn.lower()
fanNavn = fanNavn.capitalize() #Størrelsefeil fikses

sammen = navn + " " + fanNavn
print("Hvis du hadde giftet deg med idolet ditt, hadde du hett", sammen)
#I den neste deloppgaven impliseres det at man skal sette ordene sammen i ett ord. Jeg tror det kommer tydelig fram at jeg vet hvordan jeg skal gjøre det. Denne metoden røper mer håndtverk.

#Oppgave 1.7
#Nå skal variabelen "sammen" få en ny verdi:
sammen = navn + " og " + fanNavn
print("Eventuelt kan du skrive '" + str(sammen) + "' på benker og trær.") #Litt gøy må man jo ha
