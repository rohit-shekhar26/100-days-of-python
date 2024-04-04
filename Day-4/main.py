# Rock Paper Scissors

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

# put them into a list for easier access
choice_list = ['rock', 'paper', 'scissors']

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# create the option list
option_list = ['0', '1', '2']

while True:
    print("Enter user choice")
    user_input_str = input("> ")
    if user_input_str not in option_list:
        print("Invalid input. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    else:
        break

# changing the data type from str to int for user_input
user_input = int(user_input_str)
print(choice_list[user_input])

# computer choice
comp_input = random.randint(0,2)
print(choice_list[comp_input])

# evaluate the result

if user_input == comp_input:
    print("It's a tie.")
elif (user_input == 0 and comp_input == 2) or \
        (user_input == 1 and comp_input == 0) or \
        (user_input == 2 and comp_input == 1):
    print("You Win.")
else:
    print("You Lose.")