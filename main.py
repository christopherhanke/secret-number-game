from game_functions import play_game
from game_functions import show_topscore


def main():
    print("Welcome to Secret Number Game \nWhat do you want to do?")
    while True:
        print("[P]lay Game \n[S]how top scores \n[Q]uit game")
        selection = input("Your choice? ")
        selection = selection.lower()

        if selection == "p":
            print("Choose your gaming level. [H]ard or [E]asy?")
            user_level = input("Your choice? ").lower()
            if user_level == "h":
                play_game("hard")
            else:
                play_game()

        elif selection == "s":
            show_topscore()

        elif selection == "q":
            print("\nGoodbye.\n\n")
            break
        
        else:
            print("Please enter a valid option. [P/S/Q]\n\n")


if __name__ == "__main__":
    main()