import random
import time

print("{}\n{:^40}".format("*"*40, "Rock Paper Scissors Game"))
print("")
forms = ["rock","paper","scissors"]
won_games = 0
count_games = 0

#Print loading dots
def printLoading():
    for x in range(3):
        print(".", end="")
        time.sleep(0.3)

# Main game loop
while count_games<3:
    choice = random.choice(forms)

    #Receive player input
    while True:
        playerChoice = input("Choose a weapon(rock/paper/scissors): ")
        if playerChoice.lower() == "rock" or playerChoice == "paper" or playerChoice == "scissors":
            break
        else:
            print("Invalid choice. Please type either rock, paper or scissors.")
            continue
    print("{} vs {} ".format(playerChoice.capitalize(), choice.capitalize()), end="")
    printLoading()

    #Count points for win, tie or lose
    if  (playerChoice == "rock" and choice == "scissors") or (playerChoice == "scissors" and choice == "paper") or (playerChoice == "paper" and choice == "rock"):
        won_games+=1
        print(" Win!")
        count_games += 1
    elif (playerChoice==choice):
        print(" Tie!")
    else:
        print(" Lose!")
        count_games += 1

    #End game early if game is unwinnable
    if won_games == 2:
        break;

#Show game summary
print("\nYou won {}/3 games. ".format(won_games), end="") #Better luck next time
if(won_games > (count_games/2)):
    print("You win!")
else:
    print("Better Luck Next Time")
