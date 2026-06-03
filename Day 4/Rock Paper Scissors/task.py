import random
#ASCII art for rock, paper, scissors game

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

#soliciting user choice
your_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
print()

#logic for computer choice
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

# code for showing the ASCII art choice for the computer
if computer_choice == "rock":
    print(f"Computer's choice:\n {rock}")
elif computer_choice == "paper":
    print(f"Computer's choice:\n {paper}")
elif computer_choice == "scissors":
    print(f"Computer's choice:\n {scissors}")

# code for showing the ASCII art of rock, paper or scissors
if your_choice == "rock":
    print(f"Your choice:\n {rock}")
elif your_choice == "paper":
    print(f"Your choice:\n {paper}")
elif your_choice == "scissors":
    print(f"Your choice:\n {scissors}")

#logic for who wins the game using if, elif and and/or statements
if your_choice == computer_choice:
    print(f"Both of you chose {your_choice}. It's a tie!")
elif (your_choice == 'rock' and computer_choice == 'scissors') or \
     (your_choice == 'paper' and computer_choice == 'rock') or \
     (your_choice == 'scissors' and computer_choice == 'paper'):
    print(f"You chose {your_choice} and the computer chose {computer_choice}. You win!")
else:
    print(f"You chose {your_choice} and the computer chose {computer_choice}. You lose!")


#Co-Pilot's solution to the same problem
# import random
#
# choices = ['rock', 'paper', 'scissors']
# your_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
#
# if your_choice not in choices:
#     print("Invalid choice. Please enter rock, paper, or scissors.")
# else:
#     computer_choice = random.choice(choices)
#
#     if your_choice == computer_choice:
#         print(f"Both chose {your_choice}. It's a tie!")
#     else:
#         wins_against = {
#             'rock': 'scissors',
#             'paper': 'rock',
#             'scissors': 'paper'
#         }
#
#         if wins_against[your_choice] == computer_choice:
#             print(f"You chose {your_choice}, computer chose {computer_choice}. You win!")
#         else:
#             print(f"You chose {your_choice}, computer chose {computer_choice}. You lose!")