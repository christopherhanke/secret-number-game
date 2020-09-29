import random
import json

from datetime import datetime
from operator import itemgetter


class Result:
    
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date



def play_game(level="easy"):
    print(f"...initializing...\n...level: {level}... \n...Starting game...\n")
    name = input("Please login to the game with your name: ")
    print(f"\nHello {name}, great to see you.")
    print("In this game you try to find a secret number between 1 and 100.")

    secret_number = random.randint(1,100)
    attempts = 0
    guess = -1
    guesses = []

    while guess != secret_number:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid guess. (Number between 1 and 100.")
            continue

        attempts += 1

        guesses.append(guess)

        if guess < secret_number and level == "easy":
            print("Your guess is below the secret number.\n")
        elif guess > secret_number and level == "easy":
            print("Your guess is above the secret number.\n")
        else:
            print("You guessed wrong.")
    
    print("\n\nHooray, you found it!")
    print(f"The secret number is {secret_number} and you guessed {attempts} times.\n\n")

    new_score = {
        "attempts": attempts,
        "user": name,
        "level": level,
        "date": str(datetime.now()),
        "secret": secret_number,
        "guesses": guesses
    }
    score = get_score()
    score.append(new_score)

    with open("score.json", "w") as score_file:
        score_file.write(json.dumps(score))
    
    new_result = Result(score= attempts, player_name= name, date= str(datetime.now()))
    
    with open("results.txt", "w") as result_file:
        result_file.write(json.dumps(new_result.__dict__))
        
def get_score():
    try:
        with open("score.json") as score_file:
            score = json.loads(score_file.read())
    except FileNotFoundError:
        score = []
    
    return score


def get_topscores():
    score = get_score()
    topscore = sorted(score, key=itemgetter('attempts'))
    return topscore[:3]


def show_topscore():
    print("\n")
    for data in get_topscores():
        print(f"{data.get('user')} needed {data.get('attempts')} attempts. His secret number was {data.get('secret')}.")
    print("\n")
