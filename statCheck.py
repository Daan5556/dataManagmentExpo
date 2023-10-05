from textToDict import data
from textToDict import amountFiles
keys = []
for i in range(amountFiles):
    with open(r"C:\Users\egdaa\Documents\Vista 1\Expo-beoordelings project\Text to Excel\dataManagment\textFiles\keys\expoblock" + str(i + 1) + "keys.txt", "r") as file:
        for line in file:
            keys.append(line.strip())
sums = {}
for key, inner_dict in data.items():
    # Iterate through the inner dictionary
    for inner_key, value in inner_dict.items():
        # Convert the string value to integer
        numeric_value = int(value)

        # Update the sum for the inner key
        if inner_key not in sums:
            sums[inner_key] = numeric_value
        else:
            sums[inner_key] += numeric_value
print(sums)
print("Total students: " + str(len(data)))

