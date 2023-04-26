talliste = [3 , 7 , 10 , 3]
talliste.append(11)
print(talliste[0] , talliste[2])

tomListe = []
print("Skriv inn fire (4) navn")

#for i in range(4): #Gjentar alt som spesifiseres i løkken 4 ganger
#	nyttElement = input() #Tar input
#	tomListe.append(nyttElement) #Legger til input som element i listen. Det blir altså 4 elementer i listen
#print("Navnene du skrev inn var " , tomListe[0] , ", " ,  tomListe[1] , ", " ,  tomListe[2] , "og" ,  tomListe[3]) #Her kunne jeg skrevet tomListe og fått skrevet ut hele lista. Dette ser mye finere ut enn ruteklammer og hermetegn.

if ("Bendik" in tomListe):
	print("Du husket meg!")
else:
	print("Glemte du meg?")

listesum = 0
listeprodukt = 1
for i in talliste: #Løkken vil gjentas like mange ganger som det er elementer i listen, og vil for hver gjentakelse ha verdien til elementet på den plassen som telles.
	listesum += i
	listeprodukt *= i
regneliste = []
#Under legges begge utregningene til den tomme listen som er definert over.
regneliste.append(listesum)
regneliste.append(listeprodukt)
print(regneliste) #Verdiene som skrives ut stemmer over ens med kalkulator
