import random
import json

from datetime import datetime
from operator import itemgetter


class Result:
    
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date


class secret_game:
    attempts = None
    name = None
    level = None
    date = None
    _secret_number = None
    guess = None
    guesses = None

    def __init__(self):
        self._secret_number = random.randint(1,100)
        self.attempts = 0
        self.guess = -1
        self.guesses = []


    def play_game(self, level="easy"):
        self.level = level
        print(f"...initializing...\n...level: {self.level}... \n...Starting game...\n")
        self.name = input("Please login to the game with your name: ")
        print(f"\nHello {self.name}, great to see you.")
        print("In this game you try to find a secret number between 1 and 100.")

        while self.guess != self._secret_number:
            try:
                self.guess = int(input("Please enter your guess: "))
            except ValueError:
                print("Please enter a valid guess. (Number between 1 and 100.")
                continue

            self.attempts += 1

            self.guesses.append(self.guess)

            if self.guess < self._secret_number and self.level == "easy":
                print("Your guess is below the secret number.\n")
            elif self.guess > self._secret_number and self.level == "easy":
                print("Your guess is above the secret number.\n")
            else:
                print("You guessed wrong.")
        
        print("\n\nHooray, you found it!")
        print(f"The secret number is {self._secret_number} and you guessed {self.attempts} times.\n\n")

        self.date = str(datetime.now())

        score = secret_game.get_score()
        score.append(self.__dict__)

        with open("score.json", "w") as score_file:
            score_file.write(json.dumps(score))
        
            

    @staticmethod
    def get_score():
        try:
            with open("score.json") as score_file:
                score = json.loads(score_file.read())
        except FileNotFoundError:
            score = []
        
        return score


    @staticmethod
    def get_topscores():
        score = secret_game.get_score()
        topscore = sorted(score, key=itemgetter('attempts'))
        return topscore[:3]


    @staticmethod
    def show_topscore():
        print("\n")
        for data in secret_game.get_topscores():
            print(f"{data.get('name')} needed {data.get('attempts')} attempts. His secret number was {data.get('_secret_number')}.")
        print("\n")
