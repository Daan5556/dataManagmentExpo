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
    mail.Body = "Beste leerling, " + "(" + str(studentennummer) + ")" + "\n\nBij deze je beoordelingen: ""\n" + Body
    print(mail.Body)
    #mail.Send()
