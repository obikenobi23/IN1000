handleliste = {
	"melk" : "kr 14.90",
	"brød" : "kr 24.90",
	"pizza" : "kr 39.90",
} #Jeg ser at verdiene ikke skal brukes til utregning. Det gir da mer mening å gjøre tallene til strenger, slik at man kan legge til "kr" og med det tydeliggjøre at det er snakk om priser. Denne ordboka brukes nok heller som en meny eller et oppslagsverk enn en faktisk handleliste, men brukeren får ikke se navnet, så det går fint.
print(handleliste)
handleliste["frukt"] = "15.90"
handleliste["iskrem"] = "23.75"
print(handleliste) #Viser den opprinnelige listen, så legger til to elementer, så viser den igjen
