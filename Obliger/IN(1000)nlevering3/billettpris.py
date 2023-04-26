def ageism():
	aldertekst = input("Hvor gammel er du? ") #Jeg antar at bruker kjøper billetten til seg selv
	alder = int(aldertekst) #Vi kan ikke bruke tekstfilen til det vi trenger den til.
	billettpris = 0
	if (alder < 18):
		billettpris = 30
		print("Du får en barnebillett:" , billettpris , "kr")
	elif (alder > 62):
		billettpris = 35
		print("Du får honnørpris" , billettpris , "kr")
	else:
		billettpris =  50
		print("Billetten din koster" , billettpris , "kr")

	if (alder == 15):
		print("Du får denne billetten fordi du er 15 år gammel. Den koster" , billettpris ,  "kroner , forresten")
	if (alder == 31):
		print("Du får denne billetten fordi du er 31 år gammel. Den koster" , billettpris , "kroner, forresten")
	if (alder == 63 ):
		print("Gratulerer med å ha nådd pensjonsalder! Her har du billetten din.") #Jeg ser det ikke som superviktig å faktisk skrive billettprisen, da bruker ser den uansett.
ageism()
