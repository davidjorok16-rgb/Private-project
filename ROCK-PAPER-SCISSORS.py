import random
game= ("rock", "paper", "scissors")
play= random.choice(game)
guess= input("Pick a guess between rock, paper or scissors: ")
if play == guess:
    print("Tide")

elif play == "rock" and guess == "scissors":
    print("You lose")

elif play == "rock" and guess == "paper":
    print("You win")

elif play == "paper" and guess == "scissors":
    print("You win")

elif play == "paper" and guess == "rock":
    print("You lose")

elif play == "scissors" and guess == "rock":
    print("You win")

elif play == "scissors" and guess == "paper":
    print("You lose")

else:
    print("Invalid choice. Choose between rock, paper and scissors.")

while play == "paper" and guess == "rock" or play == "scissors" and guess == "paper" or play == "rock" and guess == "scissors" or play == guess:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

    play= random.choice(game)
    guess= input("Pick a guess between rock, paper or scissors: ")
    if play == guess:
        print("Tide")

    elif play == "rock" and guess == "scissors":
        print("You lose")

    elif play == "rock" and guess == "paper":
        print("You win")

    elif play == "paper" and guess == "scissors":
        print("You win")

    elif play == "paper" and guess == "rock":
        print("You lose")

    elif play == "scissors" and guess == "rock":
        print("You win")

    elif play == "scissors" and guess == "paper":
        print("You lose")

    else:
        print("Invalid choice. Choose between rock, paper and scissors.")
