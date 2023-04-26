#Deloppgave 1 og 2
print("Skriv inn et tall (du avslutter ved å skrive \"0\").")
tall = 1
talliste = []

while tall != 0:
	tall = int(input())
	if tall == 0:
		break
	talliste.append(tall)
	print("Og et til.")


#Deloppgave3
print("\nDette er tallene du skrev:")

for i in talliste:
	print(i)

#Deloppgave4
minSum = 0

for j in talliste:
	minSum += j
print("Summen av tallene er:" , minSum)


#Deloppgave5
minste_tall = talliste[0]
for k in talliste:
	if k < minste_tall:
		minste_tall = k
print("Det minste tallet du skrev var" , minste_tall)

største_tall = talliste[0]
for l in talliste:
	if l > største_tall:
		største_tall = k
print("Det største tallet du skrev var" , største_tall)

#Feilmelding hvis man skriver 0 som første tall, fordi løkkene refererer til første element, som muligens ikke finnes. Men hvis du ikke vil spille spillet, fortjener du en feilmelding.
