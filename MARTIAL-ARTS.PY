import random
game= ("block", "parry", "dodge", "punch", "kick", "special move", "resting phase", "charge")
play= random.choice(game)
guess= input("Pick a guess between block, parry, dodge, punch, kick, charge and special move: ")
health_bar_play = 100
health_bar_guess = 100
charge_play = 5
charge_guess = 5
if play == "charge" and guess == "charge" and 0 <= charge_guess < 5 and 0 <= charge_play < 5:
    print("Double Charge")
    health_bar_play -= 0
    health_bar_guess -= 0
    charge_play += 1
    charge_guess += 1

elif play == "charge" and guess == "charge" and charge_guess == 5 and charge_play == 5:
    print("Two Energy Bars Full")
    health_bar_play -= 0
    health_bar_guess -= 0
    charge_play += 0
    charge_guess += 0

elif play == "charge" and guess == "charge" and 0 <= charge_guess < 5 and charge_play == 5:
    print("Enemy Could Not Charge")
    health_bar_play -= 0
    health_bar_guess -= 0
    charge_play += 0
    charge_guess += 1

elif play == "charge" and guess == "charge" and 0 <= charge_play < 5 and charge_guess == 5:
    print("Energy Bar Full")
    health_bar_play -= 0
    health_bar_guess -= 0
    charge_play += 1
    charge_guess += 0

elif play == "special move" and guess == "special move" or play == "dodge" and guess == "dodge" or play == "parry" and guess == "parry" or play == "block" and guess == "block" or play == "punch" and guess == "punch" or play == "kick" and guess == "kick" or play == "resting phase" and guess == "resting phase":
    print("Cancel Out")
    health_bar_play -= 0
    health_bar_guess -= 0

elif play == "charge" and guess == "resting phase" and 0 <=charge_play < 5 or play == "charge" and guess == "block" and 0 <=charge_play < 5 or play == "charge" and guess == "dodge" and 0 <=charge_play < 5 or play == "charge" and guess == "parry" and 0 <=charge_play < 5:
    print("Enemy Charged")
    charge_play += 1
    health_bar_play -= 0
    health_bar_guess -= 0

elif play == "charge" and guess == "resting phase" and charge_play == 5 or play == "charge" and guess == "block" and charge_play == 5 or play == "charge" and guess == "dodge" and charge_play == 5 or play == "charge" and guess == "parry" and charge_play == 5:
    print("Enemy Could Not Charge")
    charge_play += 0
    health_bar_play -= 0
    health_bar_guess -= 0

elif guess == "charge" and play == "resting phase" and 0 <= charge_play < 5 or guess == "charge" and play == "block" and 0 <= charge_play < 5 or guess == "charge" and play == "dodge" and 0 <= charge_play < 5 or guess == "charge" and play == "parry" and 0 <= charge_play < 5:
    print("You Have A Charge")
    charge_guess += 1
    health_bar_guess -= 0
    health_bar_play -= 0

elif guess == "charge" and play == "resting phase" and charge_play == 5 or guess == "charge" and play == "block" and charge_play == 5 or guess == "charge" and play == "dodge" and charge_play == 5 or guess == "charge" and play == "parry" and charge_play == 5:
    print("Energy Bar Full")
    charge_guess += 0
    health_bar_guess -= 0
    health_bar_play -= 0

elif play == "block" and guess == "special move" and charge_guess == 5:
    print("Well Done")
    health_bar_play -= 20
    charge_guess -= 5

elif play == "block" and guess == "special move" and charge_guess < 5:
    print("Not Enough Energy")
    health_bar_play -= 0
    charge_guess -= 0

elif play == "special move" and guess == "block" and charge_play == 5:
    print("Ouch!")
    health_bar_guess -= 20
    charge_play -= 5

elif play == "special move" and guess == "block" and charge_play < 5:
    print("Close Call.")
    health_bar_guess -= 0
    charge_play -= 0

elif play == "special move" and guess == "parry" and charge_play == 5 or play == "special move" and guess == "dodge" and charge_play == 5 or play == "special move" and guess == "punch" and charge_play == 5 or play == "special move" and guess == "kick" and charge_play == 5 or play == "special move" and guess == "resting phase" and charge_play == 5 or play == "special move" and guess == "charge" and charge_play == 5:
    print("Ouch!")
    health_bar_guess -= 25
    charge_play -= 5
    charge_guess += 0

elif play == "special move" and guess == "parry" and charge_play < 5 or play == "special move" and guess == "dodge" and charge_play < 5 or play == "special move" and guess == "punch" and charge_play < 5 or play == "special move" and guess == "kick" and charge_play < 5 or play == "special move" and guess == "resting phase" and charge_play < 5 or play == "special move" and guess == "charge" and charge_play < 5:
    print("Very Close Call")
    health_bar_guess -= 0
    charge_play -= 0
    charge_guess += 0

elif guess == "special move" and play == "parry" and charge_guess == 5 or guess == "special move" and play == "dodge" and charge_guess == 5 or guess == "special move" and play == "punch" and charge_guess == 5 or guess == "special move" and play == "kick" and charge_guess == 5 or guess == "special move" and play == "resting phase" and charge_guess == 5 or guess == "special move" and play == "charge" and charge_guess == 5:
    print("Good Offense")
    health_bar_play -= 25
    charge_guess -= 5
    charge_play += 0

elif guess == "special move" and play == "parry" and charge_guess < 5 or guess == "special move" and play == "dodge" and charge_guess < 5 or guess == "special move" and play == "punch" and charge_guess < 5 or guess == "special move" and play == "kick" and charge_guess < 5 or guess == "special move" and play == "resting phase" and charge_guess < 5 or guess == "special move" and play == "charge" and charge_guess < 5:
    print("Too Bad. Not Enough Energy")
    health_bar_play -= 0
    charge_guess -= 0
    charge_play += 0

elif play == "block" and guess == "parry" or play == "block" and guess == "dodge" or play == "block" and guess == "punch" or play == "block" and guess == "kick" or play == "block" and guess == "resting phase":
    print("Oh No! Attack Blocked")
    health_bar_play -= 0

elif guess == "block" and play == "parry" or guess == "block" and play == "dodge" or guess == "block" and play == "punch" or guess == "block" and play == "kick" or guess == "block" and play == "resting phase":
    print("Good Defense")
    health_bar_guess -= 0

elif play == "parry" and guess == "resting phase" or play == "parry" and guess == "dodge" or play == "parry" and guess == "punch" or play == "parry" and guess == "kick":
    print("Too Bad. Attack Parried")
    health_bar_play -= 0

elif guess == "parry" and play == "resting phase" or guess == "parry" and play == "dodge" or guess == "parry" and play == "punch" or guess == "parry" and play == "kick":
    print("Well Done. Attack Parried")
    health_bar_guess -= 0

elif play == "dodge" and guess == "resting phase" or play == "dodge" and guess == "punch" or play == "dodge" and guess == "kick":
    print("Too Bad. Opponent Dodged")
    health_bar_play -= 0

elif guess == "dodge" and play == "resting phase" or guess == "dodge" and play == "punch" or guess == "dodge" and play == "kick":
    print("Well Done. You Dodged Attack")
    health_bar_guess -= 0

elif play == "kick" and guess == "resting phase" or play == "kick" and guess == "charge":
    print("Injured")
    health_bar_guess -= 10
    charge_guess += 0

elif guess == "kick" and play == "resting phase" or guess == "kick" and play == "charge":
    print("Well Done. You Injured Opponent")
    health_bar_play -= 10
    charge_play += 0

elif play == "punch" and guess == "resting phase" or play == "punch" and guess == "charge":
    print("Injured")
    health_bar_guess -= 5
    charge_guess += 0

elif guess == "punch" and play == "resting phase" or guess == "punch" and play == "charge":
    print("Well Done. You Injured Opponent")
    health_bar_play -= 5
    charge_play += 0

elif play == "punch" and guess == "kick":
    print("Double Injured")
    health_bar_guess -= 5
    health_bar_play -= 10

elif guess == "punch" and play == "kick":
    print("Double Injured")
    health_bar_play -= 5
    health_bar_guess -= 10  

else:
    print("Invalid choice. Choose between parry, block, dodge, punch, kick and special move.")

while 0 < health_bar_guess <= 100 and 0 < health_bar_play <= 100:
    # play_again = input("Do you want to play again? (yes/no): ")
    # if play_again.lower() != "yes":
    #     break

    play= random.choice(game)
    guess= input("Pick a guess between block, parry, dodge, punch, kick, and special move: ")
    if play == "charge" and guess == "charge" and 0 <= charge_guess < 5 and 0 <= charge_play < 5:
        print("Double Charge")
        health_bar_play -= 0
        health_bar_guess -= 0
        charge_play += 1
        charge_guess += 1

    elif play == "charge" and guess == "charge" and charge_guess == 5 and charge_play == 5:
        print("Two Energy Bars Full")
        health_bar_play -= 0
        health_bar_guess -= 0
        charge_play += 0
        charge_guess += 0

    elif play == "charge" and guess == "charge" and 0 <= charge_guess < 5 and charge_play == 5:
        print("Enemy Could Not Charge")
        health_bar_play -= 0
        health_bar_guess -= 0
        charge_play += 0
        charge_guess += 1

    elif play == "charge" and guess == "charge" and 0 <= charge_play < 5 and charge_guess == 5:
        print("Energy Bar Full")
        health_bar_play -= 0
        health_bar_guess -= 0
        charge_play += 1
        charge_guess += 0

    elif play == "special move" and guess == "special move" or play == "dodge" and guess == "dodge" or play == "parry" and guess == "parry" or play == "block" and guess == "block" or play == "punch" and guess == "punch" or play == "kick" and guess == "kick" or play == "resting phase" and guess == "resting phase":
        print("Cancel Out")
        health_bar_play -= 0
        health_bar_guess -= 0

    elif play == "charge" and guess == "resting phase" and 0 <=charge_play < 5 or play == "charge" and guess == "block" and 0 <=charge_play < 5 or play == "charge" and guess == "dodge" and 0 <=charge_play < 5 or play == "charge" and guess == "parry" and 0 <=charge_play < 5:
        print("Enemy Charged")
        charge_play += 1
        health_bar_play -= 0
        health_bar_guess -= 0

    elif play == "charge" and guess == "resting phase" and charge_play == 5 or play == "charge" and guess == "block" and charge_play == 5 or play == "charge" and guess == "dodge" and charge_play == 5 or play == "charge" and guess == "parry" and charge_play == 5:
        print("Enemy Could Not Charge")
        charge_play += 0
        health_bar_play -= 0
        health_bar_guess -= 0

    elif guess == "charge" and play == "resting phase" and 0 <= charge_guess < 5 or guess == "charge" and play == "block" and 0 <= charge_guess < 5 or guess == "charge" and play == "dodge" and 0 <= charge_guess < 5 or guess == "charge" and play == "parry" and 0 <= charge_guess < 5:
        print("You Have A Charge")
        charge_guess += 1
        health_bar_guess -= 0
        health_bar_play -= 0

    elif guess == "charge" and play == "resting phase" and charge_guess == 5 or guess == "charge" and play == "block" and charge_guess == 5 or guess == "charge" and play == "dodge" and charge_guess == 5 or guess == "charge" and play == "parry" and charge_guess == 5:
        print("Energy Bar Full")
        charge_guess += 0
        health_bar_guess -= 0
        health_bar_play -= 0

    elif play == "block" and guess == "special move" and charge_guess == 5:
        print("Well Done")
        health_bar_play -= 20
        charge_guess -= 5

    elif play == "block" and guess == "special move" and charge_guess < 5:
        print("Not Enough Energy")
        health_bar_play -= 0
        charge_guess -= 0

    elif play == "special move" and guess == "block" and charge_play == 5:
        print("Ouch!")
        health_bar_guess -= 20
        charge_play -= 5

    elif play == "special move" and guess == "block" and charge_play < 5:
        print("Close Call.")
        health_bar_guess -= 0
        charge_play -= 0

    elif play == "special move" and guess == "parry" and charge_play == 5 or play == "special move" and guess == "dodge" and charge_play == 5 or play == "special move" and guess == "punch" and charge_play == 5 or play == "special move" and guess == "kick" and charge_play == 5 or play == "special move" and guess == "resting phase" and charge_play == 5 or play == "special move" and guess == "charge" and charge_play == 5:
        print("Ouch!")
        health_bar_guess -= 25
        charge_play -= 5
        charge_guess += 0

    elif play == "special move" and guess == "parry" and charge_play < 5 or play == "special move" and guess == "dodge" and charge_play < 5 or play == "special move" and guess == "punch" and charge_play < 5 or play == "special move" and guess == "kick" and charge_play < 5 or play == "special move" and guess == "resting phase" and charge_play < 5 or play == "special move" and guess == "charge" and charge_play < 5:
        print("Very Close Call")
        health_bar_guess -= 0
        charge_play -= 0
        charge_guess += 0

    elif guess == "special move" and play == "parry" and charge_guess == 5 or guess == "special move" and play == "dodge" and charge_guess == 5 or guess == "special move" and play == "punch" and charge_guess == 5 or guess == "special move" and play == "kick" and charge_guess == 5 or guess == "special move" and play == "resting phase" and charge_guess == 5 or guess == "special move" and play == "charge" and charge_guess == 5:
        print("Good Offense")
        health_bar_play -= 25
        charge_guess -= 5
        charge_play += 0

    elif guess == "special move" and play == "parry" and charge_guess < 5 or guess == "special move" and play == "dodge" and charge_guess < 5 or guess == "special move" and play == "punch" and charge_guess < 5 or guess == "special move" and play == "kick" and charge_guess < 5 or guess == "special move" and play == "resting phase" and charge_guess < 5 or guess == "special move" and play == "charge" and charge_guess < 5:
        print("Too Bad. Not Enough Energy")
        health_bar_play -= 0
        charge_guess -= 0
        charge_play += 0

    elif play == "block" and guess == "parry" or play == "block" and guess == "dodge" or play == "block" and guess == "punch" or play == "block" and guess == "kick" or play == "block" and guess == "resting phase":
        print("Oh No! Attack Blocked")
        health_bar_play -= 0

    elif guess == "block" and play == "parry" or guess == "block" and play == "dodge" or guess == "block" and play == "punch" or guess == "block" and play == "kick" or guess == "block" and play == "resting phase":
        print("Good Defense")
        health_bar_guess -= 0

    elif play == "parry" and guess == "resting phase" or play == "parry" and guess == "dodge" or play == "parry" and guess == "punch" or play == "parry" and guess == "kick":
        print("Too Bad. Attack Parried")
        health_bar_play -= 0

    elif guess == "parry" and play == "resting phase" or guess == "parry" and play == "dodge" or guess == "parry" and play == "punch" or guess == "parry" and play == "kick":
        print("Well Done. Attack Parried")
        health_bar_guess -= 0

    elif play == "dodge" and guess == "resting phase" or play == "dodge" and guess == "punch" or play == "dodge" and guess == "kick":
        print("Too Bad. Opponent Dodged")
        health_bar_play -= 0

    elif guess == "dodge" and play == "resting phase" or guess == "dodge" and play == "punch" or guess == "dodge" and play == "kick":
        print("Well Done. You Dodged Attack")
        health_bar_guess -= 0

    elif play == "kick" and guess == "resting phase" or play == "kick" and guess == "charge":
        print("Injured")
        health_bar_guess -= 10
        charge_guess += 0

    elif guess == "kick" and play == "resting phase" or guess == "kick" and play == "charge":
        print("Well Done. You Injured Opponent")
        health_bar_play -= 10
        charge_play += 0

    elif play == "punch" and guess == "resting phase" or play == "punch" and guess == "charge":
        print("Injured")
        health_bar_guess -= 5
        charge_guess += 0

    elif guess == "punch" and play == "resting phase" or guess == "punch" and play == "charge":
        print("Well Done. You Injured Opponent")
        health_bar_play -= 5
        charge_play += 0

    elif play == "punch" and guess == "kick":
        print("Double Injured")
        health_bar_guess -= 5
        health_bar_play -= 10

    elif guess == "punch" and play == "kick":
        print("Double Injured")
        health_bar_play -= 5
        health_bar_guess -= 10  

    else:
        print("Invalid choice. Choose between parry, block, dodge, punch, kick and special move.")

if 0 < health_bar_guess <= 100 and health_bar_play <= 0:
    print("K.O. YOU WOOOOOOOOON!")
    print(health_bar_guess)
else:
    print("YOU LOSE")
    print(health_bar_play)
