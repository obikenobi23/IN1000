fahr = float(input("Hvor varmt er det? (Fahrenheit)")) #fahr lagres som et tall. int() virket ikke med formatteringen under, så da ble det float().
print("Grader i fahrenheit: " , fahr)

cels = ((fahr) - 32) * 5 / 9
print("{:.2f}".format(cels)) #Formaterer cels til å vise et fornuftig antall sifre.
