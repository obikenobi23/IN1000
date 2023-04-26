#Oppgave 3.3
#Hvis man skal skive en hel dato som et heltall, er det viktig å passe på at den primære ordningen får høyest verdi. Da setter vi altså måned først.
print("Skriv en dato på formen MMDD (eks: 0830= 30. august)")
dato1 = input()

print("Skriv inn en ny dato på samme form")
dato2 = input()

if(dato1 < dato2):
	print("Riktig rekkefølge!")
elif(dato1 > dato2):
	print("Feil rekkefølge!")
elif(dato1 == dato2):
	print("Samme dato!")
else:
	print("Dette er skrevet feil.")
#Jeg ser nå at å slå sammen dato og måned i den forrige oppgaven hadde spart mye arbeid.
