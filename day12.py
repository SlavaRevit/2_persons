import random
import sys
EASY_MODE = 10
HARD_MODE = 5

# print("Hello to the gussing game")
print("""
   ▄██████▄  ███    █▄     ▄████████    ▄████████    ▄████████  ▄█  ███▄▄▄▄      ▄██████▄          ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄   ███    ███        ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ 
  ███    █▀  ███    ███   ███    █▀    ███    █▀    ███    █▀  ███▌ ███   ███   ███    █▀         ███    █▀    ███    ███ ███   ███   ███   ███    █▀  
 ▄███        ███    ███  ▄███▄▄▄       ███          ███        ███▌ ███   ███  ▄███              ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄     
▀▀███ ████▄  ███    ███ ▀▀███▀▀▀     ▀███████████ ▀███████████ ███▌ ███   ███ ▀▀███ ████▄       ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀     
  ███    ███ ███    ███   ███    █▄           ███          ███ ███  ███   ███   ███    ███        ███    ███   ███    ███ ███   ███   ███   ███    █▄  
  ███    ███ ███    ███   ███    ███    ▄█    ███    ▄█    ███ ███  ███   ███   ███    ███        ███    ███   ███    ███ ███   ███   ███   ███    ███ 
  ████████▀  ████████▀    ██████████  ▄████████▀   ▄████████▀  █▀    ▀█   █▀    ████████▀         ████████▀    ███    █▀   ▀█   ███   █▀    ██████████ 
                                                                                                                                                       
""")
print("I'm thinking about a number between 1 and 100")

game_mode = input("Chose a diffuculty. Type 'easy' or 'hard: ")
play_game = True



def create():
    if game_mode == 'easy':
        return EASY_MODE
    else:
        return HARD_MODE

def game():
    global attempts
    global play_game
    if attempts <= 0:
        print("You run out of attempts")
        play_game = False
    elif make_a_guess == computer_number:
        print(f"You are right, its: {make_a_guess} ")
        play_game = False
    elif make_a_guess != computer_number and make_a_guess > computer_number:
        attempts -= 1
        print("Too high")
        print(f"You have left {attempts} attempts ")
    elif make_a_guess != computer_number and make_a_guess < computer_number:
        attempts -= 1
        print("Too low")
        print(f"You have left {attempts} attempts ")

guess = create()
attempts = guess
print(f"You have {attempts} attempts ramaining to guess the number.")
computer_number = random.randint(1,100)


while play_game:
    make_a_guess = int(input("Make a guess: "))
    game()



    