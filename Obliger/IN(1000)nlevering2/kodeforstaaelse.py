#Koden er ikke lovlig. Så lenge inputet gis riktig av bruker, vil b kunne konverteres til en heltallsvariabel som gir det samme outputet som strengvariabelen a. Beslutningen krever ingen "else" for å virke: Et eventuelt brudd på beslutningen vil gi ingen resultat. Problemet oppstår i den fjerde linjen. b er ikke en strengvariabel, og kan derfor ikke settes sammen med strengen. Dette kan løses ved å kombinere komponentene med et komma i stedet for et plusstegn, eller ved å bruke variabel a i stedet for b.

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
	print (b + "Hei!")
