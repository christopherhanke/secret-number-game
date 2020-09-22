import random
import json

from datetime import datetime

# initializing
secret = random.randint(1, 100)
attempts = 0
guess = -1
score = []
score_avaible = True

# welcome on screen
print("\n\nHello and welcome to the secret number game.")

# try to open the score or going first player
try:
    with open("score.txt", "r") as score_file:
        score = json.loads(score_file.read())
        
except FileNotFoundError:
    print("Your the first player and will start a new score table.")
    with open("score.txt", "w+") as score_file:
        score_file.write("[]")
        score_avaible = False

if score_avaible:
    print("The users before you, left this scores.")
    for data in score:
        print(f"{data.get('attempts')} Attempts at {data.get('date')}.")

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

    # hint the secret
    if guess < secret:
        print("Your guess is below the secret number.\n")
    if secret < guess:
        print("Your guess is above the secret number.\n")

# secret number achieved
print("\n\nHooray, you found it!")
print(f"The secret number is {secret} and you guessed {attempts} times.")

new_score = {"attempts": attempts, "date": str(datetime.now())}
score.append(new_score)

# writing to the score data
with open("score.txt", "w") as score_file:
    score_file.write(json.dumps(score))
