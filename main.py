# Import the random module here
import random
# Split string method
totalnames = []
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# totalnames.extend(names)
# totalnama = len(names)
# bayar = random.randint(1, totalnama)
# print()
totalnama = len(names)
bayar = random.randint(0, totalnama)
byr = names[bayar]
print(byr + " is going to Pay the bill today.")