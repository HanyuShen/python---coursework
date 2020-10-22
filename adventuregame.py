import time,os
print("Loading.....")
time.sleep(2)





print("Welcome to my game!" + os.getlogin() + "\nPlease choose a character: ")


characterList = ["Knight","Warrior","Wizard"]

i = 0
while i< len(characterList):
    print(str(i + 1)+ "." + characterList[i])
    i += 1
    

character = int(input("Type in your character number: "))


selectedCharacter = characterList[character - 1]

print("You chose: " + selectedCharacter)
