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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
### courtesy ascii.co.uk/art
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a beach.  A cove is on the left and a jungle is on the right.  Where do you go? \n")
if direction == 'left':
  swim_or_wait = input("You found a lagoon with an island in the middle of it.  Do you swim to it or wait for a boat? \n")
  if swim_or_wait.lower() == 'wait':
    door_choice = input("A boat drifts by and you make it to the island. On the ground there are what appear to be three storm shelter doors, each a different color.  Do you choose the red, blue, or yellow door? \n")
    if door_choice.lower() == 'red':
      print("It\'s a room full of fire. Game Over.")
    elif door_choice.lower() == 'blue':
      print("You enter a room of beasts. Game Over.")
    elif door_choice.lower() == 'yellow':
      print("You found the treasure! You Win!")
    else:
      print("You chose a door that doesn\'t exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
