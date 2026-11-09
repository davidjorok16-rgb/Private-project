import random
game = ("head", "tail")
play = random.choice(game)
guess = input("Choose a guess between head and tail:")
if play == guess:
    print("You win")
else:
    print("You lose")