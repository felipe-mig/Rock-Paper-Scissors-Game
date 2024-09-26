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
# rock = [0]; paper [1]; scissors[2]
game_images = [rock, paper, scissors]

user_choice = int(input("Choose scissors, paper or rock. Type: 0 for rock; 1 for paper; 2 for scissors\n"))
# Here we are printing the images based on their index and the variable user_choice
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"computer chose:")
# Here we are printing the images based on their index and the variable computer_choice
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("you lose...")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It is a draw")

elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose...")
