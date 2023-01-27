import random
import time
winningCombinations = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def main():
    #forms = ["rock", "paper", "scissors"]
    show_decorations()
    won_games = game_loop()
    show_summary(won_games)

def show_decorations():
    print("{}\n{:^40}\n".format("*" * 40, "Rock Paper Scissors Game"))

def show_loading():
    for x in range(3):
        print(".", end="")
        time.sleep(0.3)

def game_loop():
    count_games = 0
    won_games = 0
    while count_games < 3:
        choice = random.choice(list(winningCombinations.keys()))
        playerChoice = ""
        try:
            playerChoice = input("Choose a weapon(rock/paper/scissors): ")
            if playerChoice.lower() not in ["rock", "paper", "scissors"]:
                raise ValueError("Invalid choice. Please type either rock, paper or scissors.")
        except ValueError as e:
            print(e)
            continue

        print("{} vs {} ".format(playerChoice.capitalize(), choice.capitalize()), end="")
        show_loading()

        #Count points for win, tie or lose
        if winningCombinations[playerChoice] == choice: #if (playerChoice, choice) in [("rock","scissors"),("paper","rock"),("scissors","paper")]:
            won_games += 1
            print(" Win!")
            count_games += 1
        elif (playerChoice == choice):
            print(" Tie!")
        else:
            print(" Lose!")
            count_games += 1

        #End unwinnable game
        if won_games == 2:
            break
    return won_games

def show_summary(won_games):
    print("\nYou won {}/3 games. ".format(won_games), end="")  # Point 5
    if (won_games >= 2):
        print("You win!")
    else:
        print("Better Luck Next Time")

if __name__  == "__main__":
    main()
