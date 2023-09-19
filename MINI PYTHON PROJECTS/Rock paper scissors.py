import random

user_wins = 0
computer_wins = 0
draw_game = 0
options = ["rock","paper","scissors"]

print("~" * 38)
print("WELCOME TO ROCK PAPER SCISSORS GAME".center(38))
print("~" * 38)

input("Press enter to start: ")

while True:
    user_input = input("\nType rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked",computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "paper":
        print("You draw!")
        draw_game += 1
    
    elif user_input == "rock" and computer_pick == "rock":
        print("You draw!")
        draw_game += 1
    
    elif user_input == "scissors" and computer_pick == "scissors":
        print("You draw!")
        draw_game += 1        
    
    else:
        print("You lost!")
        computer_wins += 1


print("\n" + "-" * 43)
if user_wins > computer_wins:
    print("Good job!,You won the overall game".center(43))

elif user_wins < computer_wins:
    print ("You lost the overall game,try again later".center(43))

elif user_wins == computer_wins:
    print("Nice work, You draw the overall game".center(43))
print("-" * 43)

print("\nYou won:",user_wins,"times.")
print("You lost:",computer_wins,"times.")
print("You draw:",draw_game,"times.")









