import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0,2)

if choice == 0:
  print(rock)
  print("\n")
elif choice == 1:
  print(paper)
  print("\n")
else:
  print(scissors)
  print("\n")

print("Computer chose:\n")

if computer_choice == 0:
  print(rock)
  print("\n")
elif computer_choice == 1:
  print(paper)
  print("\n")
else:
  print(scissors)
  print("\n")

if choice == computer_choice:
  print("It's a draw")
elif choice == 0 and computer_choice == 1:
  print("Rock loses to paper.  Try again")
elif choice == 0 and computer_choice == 2:
  print("Rock smashes scissors.  You win!")
elif choice == 1 and computer_choice == 0:
  print("Paper covers rock.  You win!")
elif choice == 1 and computer_choice == 2:
  print("Paper gets cut by scissors.  Try again")
elif choice == 2 and computer_choice == 0:
  print("Scissors gets smashed by rock.  Try again")
elif choice == 2 and computer_choice == 1:
  print("Scissors cuts paper.  You win!")
else user_choice > 2:
  print("You didn't make a correct choice.  Run the program again.")
