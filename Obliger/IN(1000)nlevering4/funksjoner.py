#Deloppgave 1
def adder (tall1 , tall2):
	sum = tall1 + tall2
	return sum

#Her printes funksjonene, med argumenter lagt i print-funksjonen.
print(adder(5 , 4))
print(adder(7 , 3))


#Deloppgave 2
def tellForekomst ():
    #Definerer argumenter som tas i bruk i funksjonen
	ord = input("Hei! Skriv inn et ord og et tegn. ")
	bokstav = input()
	tegnteller = 0

#Deloppgave 3
    #Teller gjennom tekststrengen som mates inn for å lete etter likheter, teller dem opp
	for tegn in ord:
		if tegn == bokstav:
			tegnteller += 1
	#Gir et tilpasset svar avhengig av utfallet
	if tegnteller == 0:
		print(bokstav, "finnes ikke i det ordet.")
	else:
		print("Tegnet", bokstav, "dukker opp", tegnteller, "ganger i ", ord)
		return tegnteller

tellForekomst()
