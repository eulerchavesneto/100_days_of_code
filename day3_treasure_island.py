print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")

direction = input("Which way do you want to go? LEFT or RIGHT")
direction = direction.lower()

if direction == "left":
    direction = input("You found a river. Do you want to SWIM or WAIT for a boat?")
    direction = direction.lower()
    if direction == "wait":
        direction = input("You found 3 doors! Which one do you choose? RED, BLUE or YELLOW?")
        direction = direction.lower()
        if direction == "yellow":
            print("You found the gold! You won the game! Congratulations!")
        elif direction == "red":
            print("Burned by fire. Game over!")
        elif direction == "blue":
            print("Eaten by beasts. Game over!")
        else:
            print("Game Over!")
    else:
        print("You were attacked by trout. Game over!")
else:
    print("You fall into a hole. Game over!")

