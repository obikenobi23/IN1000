ord = input("Skriv inn et ord. ")
#ord = "Banankake" #For enkel testing


def ord_lengde(ord):
	return len(ord)


print(ord_lengde(ord))


#setning = input("Skriv en tekst. Det kan være en påstand, en oppskrft eller et eventyr. Unngå stor bokstav og tegnsetting for best resultat. ")
setning = "det var en gang en liten gutt som het Bendik" #Input-fritt alternativ


def setningssplitter(setning):
	split = setning.split() #Gjør strengen om til en liste, der hvert ord blir et element.
	split.sort() #Elementene sorteres alfabetisk

	#Et par tomme variabler som skal brukes senere
	tallListe = []
	dict = {}

	mengde = set(split) #Her elimineres gjentakninger, slik at vi står igjen med én iterasjon av hvert element
	utenRepetisjon = list(mengde) #Mengden uten repetisjoner gjøres om til en liste som kan sorteres alfabetisk
	utenRepetisjon.sort() #Listen uten repetisjoner sorteres alfabetisk

	for i in range(len(split)): #Her bygger vi listen tallListe, som til slutt skal ha ett element for hvert unike ord. Altså like mange elementer som den repetisjonsløse listen.
		if split[i] == split[i - 1]: #Hvis elementet er lik forrige element i lista: Legg til 1 på verdien i talliste. Siden "split" er ordnet alfabetisk, kan man sammenlikne med elementet i forrige indeks. Tallet i en gitt indeks i tallListe er altså antallet ganger ordet fra samme indeks i utenRepetisjon har oppstått i steningen.
			tallListe[len(tallListe) - 1] += 1
#            print("jess") #En bugtest som viser hver gang et ord gjenoppstår
		else: #Hvis elementet som sjekkes ikke har vært der før, får listen et nytt element, som alltid er tallet 1. Antallet elementer blir da antallet unike ord.
			tallListe.append(1)
#            print("nope") #Bugtest som viser når et ord oppstår for første gang.
	for j in range(len(tallListe)): #Legger til hvert ord som en egen nøkkel, og antallet repetisjoner som tilsvarende verdi.
		dict[utenRepetisjon[j]] = tallListe[j]


	#Her skrives alle variablene for å sjekke at programmet og jeg er enige etter at alt er sagt og gjort.
	print("split: ", split)
	print("tallListe: ", tallListe)
	print("mengde: ", mengde)
	print("Liste uten repetisjon: ", utenRepetisjon)
	print("dict: ", dict)

	for key in sorted(dict, key=dict.get, reverse = True): #Sorterer ordboka etter verdier i synkende rekkefølge (ordet som oppstår flest ganger kommer øverst)
		print(key , dict[key])


setningssplitter(setning)
