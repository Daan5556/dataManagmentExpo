from textToDict import data
import win32com.client as win32

amountOfStudents = len(data.keys())
listOfStudents = list(data.keys())

for i in range(amountOfStudents):
    studentennummer = listOfStudents[i]
    mail_adress = str(studentennummer) + "@vistacollege.nl"
    ratings = data[studentennummer]
    body_ratings = []
    for j in ratings:
        body_ratings.append(str(j) + ": " + str(ratings.get(j)))
    Body = "\n".join(body_ratings)
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = str(mail_adress)
    mail.Subject = "Terugkoppeling Expo Beoordelingen"
    mail.Body = "Beste leerling, " + "(" + str(studentennummer) + ")" + "\n\nBij deze de beoordelingen: ""\n" + Body + "\n\nMet vriendelijke groet,\n\nDaan Eggen\n\nBedankt dat je hebt meegedaan aan mijn test! Ik ben bezig met een product te maken voor school, zodat leerlingen beoordelingen kunnen geven aan expo's. Deze beoordelingen worden opgeslagen in een database voor docenten. Ook stuurt het automatisch de data terug naar het ingevulde leerlingnummer. Het ontvangen van deze mail betekend dat de test goed is verlopen. Ik ontvang graag feedback van jou over mijn product, deze kan je mij sturen op dit mailadres.\n\nEr hebben 19 leerlingen meegedaan aan de test. Dit gebeurde in 2 tijdsblokken met verschillende expo's. Expo Avocado scoorde het laagste met een gemiddelde rating van 1,4 & expo Aardbei het hoogste met een rating van 2,5."
    print(mail.Body)
    #mail.Send()
