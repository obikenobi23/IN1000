matplan = {
	"Esther" : ["brødskiver" , "kjøttboller" , "corn flakes"] ,
	"Ståle" : ["havregrøt" , "fiskegrateng" , "tomatsuppe"] ,
	"Gyda" : ["knekkebrød" , "enchiladas" , "én rå potet"]
}
def tabell():
	print("Dette er beboerne våre: " , matplan.keys())
	beboerNavn = input("Hvilken beboer vil du vite matplanen til? ")
	if (beboerNavn in matplan):
		print("Dette er" , beboerNavn , "sin matplan: " , matplan[beboerNavn])
	else:
		print("Dette er ikke navnet på noen av beboerne våre.")
tabell()

#Deloppgave 3
#a) Brukernavn kan lett lagres i en liste. Hvis det ikke kreves ekstra informasjon er lister en fin måte å lagre en rekke med like datamengder. Siden listen skal oppdateres hvert år, kan vi ikke bruke en mengde.
#b) Når en verdi skal knyttes sammen med en eller flere andre er det mer nyttig å bruke en ordbok.
#c) Med kun navn er vi i samme situasjon som i a). Siden informasonen skal oppdateres, som i a), er det ingen grunn til å velge noe annet.
#d) Her ser vi også på en rekke med enkeltstående verdier. Men i motsetning til a) og c) skal ikke denne listen endres i særlig grad. I tillegg er den nok betydelig kortere, så rekkefølgen vil ikke være av stor verdi. Allergener pleier meg kjent ikke å listes i noen spesifikk rekkefølge. Da er mengde et godt valg for denne typen. Skjønt både i a), c) og d) vil ikke det å bytte mellom liste og mengde ødelegge noe.
