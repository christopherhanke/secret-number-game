import random

# initializing
secret = random.randint(1, 100)
attempts = 0
guess = -1
score_avaible = True

# welcome on screen
print("\n\nHello and welcome to the secret number game.")

# try to open the score or going first player
try:
    with open("score.csv", "r") as score_data:
        score = score_data.read()
        print(f"Till now the best player needed {score} guess attempts.")
except FileNotFoundError:
    print("Your the first player and will start a new score table.")
    score_avaible = False

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

# writing to the score data
if score_avaible:
    with open("score.csv", "a") as score_data:
        score_data.write(f",{str(attempts)}")
else:
    with open("score.csv", "w") as score_data:
        score_data.write(f",{str(attempts)}")
