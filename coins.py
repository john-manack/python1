# Ex. M - 3

# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program.


coins = 0
quest = input("You have " + str(coins) + " coins. Would you like another? Type 'yes' or 'no':")
quest = quest.lower()

while quest != 'yes' and quest != 'no':
    quest = input("Sorry - you must ender 'yes' or 'no'. You have " + str(coins) + " coins. Would you like another? Type 'yes' or 'no':")
    quest = quest.lower()

while quest == 'yes':
    coins += 1
    quest = input("You have " + str(coins) + " coins. Would you like another? Type 'yes' or 'no':")
    quest = quest.lower()
    
print("Bye")