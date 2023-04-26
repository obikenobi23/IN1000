#Deloppgave 1
#steder = ["Marrakesh" , "Tokyo" , "Athen" , "Kario" , "Paris"]
steder = [] #Tom liste her, men hvis du kan endre koden slipper du å skrive så sykt mye.

for i in range(5): #Legger til fem strenger, helst stedsnavn
	nytt_sted = input("Legg til en reisedestinasjon i reiseplanen. ")
	steder.append(nytt_sted)



#Deloppgave 2
#klesplagg = ["solbriller" , "shorts" , "sandaler" , "solhatt" , "skjorte"]
klesplagg = [] #Brukervennlighet vettu

for j in range(5): #Legger til fem strenger, helst navn på klesplagg
	nytt_klesplagg = input("Hva vil du ha på deg på reisen? ")
	klesplagg.append(nytt_klesplagg)

#avreisedatoer = ["3. august" , "15.august" , "27. august" , "1. september" , "5. september"]
avreisedatoer = [] #Du skjønner greia

for k in range(5): #Legger til fem sternger, med en oppfordring til hvordan man bruker programmet
	ny_dato = input("Legg til en mulig avreisedato. Bruk formen DD.måned.")
	avreisedatoer.append(ny_dato)



#Deloppgave 3
reiseplan = [steder , klesplagg , avreisedatoer] #Alle listene havner i én liste, der man kan aksessere (finne?) hvert element gjennom å oppgi to indekser.



#Deloppgave 4
for l in range(len(reiseplan)):
	print(reiseplan[l]) #Bruker får se hele reiseplanen



#Deloppgave 5
plassref = input("Hvilken liste vil du finne? (1 til 3) ")
elementref = input("Hvilken plass i listen vil du oppsøke? (1 til 5) ") #Dette er de to indeksene som nevnt
indeks1 = int(plassref) - 1
indeks2 = int(elementref) - 1 #Siden det er mange elementer å holde styr på, gjør jeg omregningen fra vanlig norsk referering til datareferering for bruker. Det er ikke i henhold til oppgaveteksten, men det er brukervennlig.

if indeks1 not in reiseplan or indeks2 not in reiseplan: #Hvis én av inputene ikke finnes i verdiområdet, gi feilmelding. Ellers skriv ut elementet.
    print("Programmet mottok ikke en lokasjon i listen. ")
else:
    print(reiseplan[indeks1][indeks2]) #Og her er magnum opus: To indekser etter hverandre
