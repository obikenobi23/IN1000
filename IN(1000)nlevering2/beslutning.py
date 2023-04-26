#Skriv et program der maskinen kan bestemme en persons kulhetsgrad utifra hvilke serier personen har sett.

poeng = 0

GoT = input("Har du sett Game of Thrones? ")
if (GoT == "ja"):
	print("Bra.")
	poeng += 1
#Denne litt rotete metoden med å flette beslutningen inn i spørsmålene sørger for at bruker får øyeblikkelig svar.

CK = input("Har du sett Cobra Kai? ")
if (CK == "ja"):
	print("Bra.")
	poeng += 1

BBMF = input("Har du sett Beyblade: Metal Fusion? ")
if (BBMF == "ja"):
	print("LOL er du 5 år eller?")
else:
	print("Bra.")
	poeng += 1
print("Du fikk " , str(poeng) , " poeng.")
#Feilaktige svar vil i de flest tilfeller telles som et "nei", noe som kanskje er uheldig. I det siste spørsmålet vil et tilfeldig svar telles som "ja" og gi poenguttelling, noe som er ekstra uheldig. Dette kan lett fikses, men jeg anser det ikke som nødvendig for oppgaven.
