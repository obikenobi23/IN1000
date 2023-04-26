#Oppgave 2.1
print("Kunne du tenke deg en brus? (ja/nei)")
svar = input()
#Tydeliggjør hva som er gyldig respons. Tar også inn svaret på en annen linje enn spørsmålet står på.

#Oppgave 2.2
svar = svar.lower()
#Fjerner caps-sensitivitet før inputet brukes. Så vil ja/Ja/jA/JA tolkes som "ja" i beslutningen:
if(svar == "ja"):
	print("Her har du en brus!")
elif(svar == "nei"):
	print("Den er grei.")
else:
	print("Det forstod jeg ikke helt")
#Her tas inputene som brukeen fikk vite at er gyldige, og brukes til å simulere en slags samtale. Alle andre svar havner i "else:".
