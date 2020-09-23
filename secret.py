import random
import json

from datetime import datetime
from operator import itemgetter

# initializing
secret = random.randint(1, 100)
attempts = 0
guess = -1
guesses = []
score = []
score_avaible = True
question = None

# welcome on screen
print("\n\nWelcome to the secret number game.")

#login with user name
name = input("Please login with your name: ")
print(f"\nHello {name}, great to see you.")


# try to open the score or going first player
try:
    with open("score.txt", "r") as score_file:
        score = json.loads(score_file.read())
        
except FileNotFoundError:
    print("Your the first player and will start a new score table.")
    with open("score.txt", "w+") as score_file:
        score_file.write("[]")
        score_avaible = False


# show score list, if player wants it
if score_avaible:
    while question != "y" and question !="n":
        question = input("Do you wanna see the top three scores? [y/n] ")
        question = question.lower()

    if question == "y":
        #sorting score list using players attempts
        best_list = sorted(score, key=itemgetter('attempts'))
        
        #printing top three scores of attempts
        print("Top Three Scores")
        for data in best_list[:3]:
            print(f"{data.get('user')} needed {data.get('attempts')} Attempts, at {data.get('date')}.")


# loop the guesses till secret number is found
while guess != secret:
    if attempts == 0:
        try:
            guess = int(input("What's your first guess? "))
        except ValueError:
            print("Please enter a valid guess. (Number between 1 and 100)")
            continue
    else:
        try:
            guess = int(input("What's your next guess? "))
        except ValueError:
            print("Please enter a valid guess. (Number between 1 and 100)")
            continue
    
    # iterate attempts
    attempts += 1

    #save guesses
    guesses.append(guess)

    # hint the secret
    if guess < secret:
        print("Your guess is below the secret number.\n")
    if secret < guess:
        print("Your guess is above the secret number.\n")


# secret number achieved and game ending
print("\n\nHooray, you found it!")
print(f"The secret number is {secret} and you guessed {attempts} times.")


# saving score
new_score = {"attempts": attempts, "user": name, "date": str(datetime.now()), "secret": secret, "guesses": guesses}
score.append(new_score)

# saving to file
with open("score.txt", "w") as score_file:
    score_file.write(json.dumps(score))
