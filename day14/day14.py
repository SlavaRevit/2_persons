import random
from data import data
import click



score = 0 
player1 = random.choice(data)
player2  = random.choice(data)
print(f"Compare A: {player1['name']}, {player1['description']}, {player1['country']}")
print(f"Compare B: {player2['name']}, {player2['description']}, {player2['country']}")
guess = input("Who has more followers: 'A' or 'B'? ")

def compare(player1, player2):
    global score
    folowers_player1 = player1['follower_count']
    folowers_player2 = player2['follower_count']
    
    print(folowers_player1, folowers_player2)
    
    if guess == "A":
        if folowers_player1 > folowers_player2:
            score += 1
            click.clear()
        else:
            click.clear()
            print(f"Sorry, that's wrong. Final score {score}")
    elif guess == "B":
        if folowers_player2 > folowers_player1:
            score += 1
            print(score)

compare(player1=player1, player2=player2)
# def check_answer()


# compare(player1=player1, player2=player2)
# play_again = True
# while play_again:



