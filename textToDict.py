import os
data = {}

# checks amount of textfiles in directory
amountFiles = 0
directory = r"C:\Users\egdaa\Documents\Vista 1\Expo-beoordelings project\Text to Excel\dataManagment\textFiles"
for path in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, path)):
        amountFiles += 1

for i in range(amountFiles):
    # checks amount of lines, expo's and students
    # makes list of studentnumbers # makes list of ratings
    with open(r"C:\Users\egdaa\Documents\Vista 1\Expo-beoordelings project\Text to Excel\dataManagment\textFiles\expoblock" + str(i + 1) + ".txt", "r") as file:
        lineCount = 0
        studentList = []
        ratingList = []
        for line in file:
            lineCount += 1
            if len(line) > 3:
                studentList.append(line.strip())
            else:
                ratingList.append(line.strip())
        studentCount = len(studentList)
        expoCount = lineCount / studentCount - 1
    # makes list of keys
    keys = []
    with open(r"C:\Users\egdaa\Documents\Vista 1\Expo-beoordelings project\Text to Excel\dataManagment\textFiles\keys\expoblock" + str(i + 1) + "keys.txt", "r") as file:
        for line in file:
            keys.append(line.strip())
    # creates dictionary from file
    for j in range(studentCount):
        studentnummer = studentList[j]
        entry = {}
        for x in range(int(expoCount)):
            key = keys[x]
            ratingIndex = j * expoCount + x
            entry[key] = ratingList[int(ratingIndex)]
        # puts dictionary in data {}
        if (studentnummer) in data.keys():
            data[studentnummer].update(entry)
        else:
            data[studentnummer] = entry
