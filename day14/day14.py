import random
from data import data
import click


def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
 
def check_answer(guess, folowers_player1, folowers_player2):
    if folowers_player1 > folowers_player2:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()
         
        print(f"Compare A: {format_data(account_a)}.")
        # print(vs)
        print(f"Compare B: {format_data(account_b)}.")
        
        guess = input("Who has more folowers? Type 'A' or 'B': ").lower()
        
        a_folower_count = account_a['follower_count']
        b_folower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_folower_count, b_folower_count)
        click.clear()
        print("Logo")
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}. ")
        else:
            game_should_continue = False
            print(f"Sorry , that's wrong. Final score: {score}")

game()