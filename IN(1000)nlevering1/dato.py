#Oppgave 3.1
#Tolker oppgaven som at man skal lage fire separate inputs; to for dag og to for måned.

print("Kan du skrive inn en dato? (tall fra 1 til 31)")
dato1 = input()
print("Kan du skrive inn en måned? (tall fra 1 til 12)")
måned1 = input()
#Dette blir dato og måned for den første datoen.

print("Kan du skrive inn en annen dato? (tall fra 1 til 31)")
dato2 = input()
print("Kan du skrive inn en annen måned? (tall fra 1 til 12)")
måned2 = input()
#Copy-paste er programmererens beste venn

#Oppgave 3.2
if(måned1 < måned2):
	print("Riktig rekkefølge!")
elif(måned1 > måned2):
	print("Feil rekkefølge!")
elif(måned1 == måned2):
	if(dato1 < dato2):
		print("Riktig rekkefølge!")
	elif(dato1 > dato2):
		print("Feil rekkefølge!")
	elif(dato1 == dato2):
		print("Samme dato!")
	else:
		print("Dette er skrevet feil.")
else:
	print("Dette er skrevet feil.")
#Dette programmet sjekker først om månedene er like (de har mest å si for datoen), så om datoene er like. Hvis den ene måneden er større enn den andre er rekkefølgen uavhengig av datoene. Programmet vil bare sjekke datoene om månedene er like (måned1 ikke større eller mindre enn måned2 -> de er like store).
