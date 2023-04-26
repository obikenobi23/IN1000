#Lag en interaktiv handleliste som tar imot input om spesifikke varer og gir "kunden" en pris basert på varene som kjøpes.
def matvarer():
	varebeholdning = {
	"egg" : 5 ,
	"melk" : 10 ,
	"hermetikk" : 20 ,
	"lasagne" : 30 ,
	"grønnsaker" : 15 ,
	"juice" : 20 ,
	"frukt" : 15 ,
	"ris" : 10 ,
	"kjøttdeig" : 20
	}
	handleliste = []
	pris = 0
	print("Dette er varene våre:", varebeholdning.keys())
	valg = int(1)
	while valg == 1:
		print(valg)
		print("Hvilken matvare vil du legge til i handlelisten?")
		tillegg = input()
		if(tillegg in varebeholdning):
			handleliste.append(tillegg)
			pris += varebeholdning[tillegg]
			valg = int(input("Vil du legge til en vare til? (1 = ja, 0 = nei)"))
		else:
			print("Vi har ikke den varen. Prøv noe annet.")
	else:
		print("Dette er varene du har kjøpt: ", str(handleliste))
	print("Dette er prisen på dem: " , str(pris))
matvarer()
