import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type an integer!")
    

random_number = random.randint(0, top_of_range)
guesses = 0 

while True:
    guesses += 1
    user_guesses = input("Make a guess: ")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print("Please type an integer!")
        continue

    if user_guesses == random_number:
        print("You got it!")
        break
    elif user_guesses > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "movement")    
            
































