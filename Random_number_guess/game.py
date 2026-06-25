import random

print("WELCOME TO THE NUMBER GUESSING GAME!")

secret_number = random.randint(1, 100)

guess = int(input("Guess a number (1 - 100): "))
while True:
    print(f"You guessed: {guess}")
    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.\n")
        break
    
    elif guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        direction = "lesser than" if guess < secret_number else "more than"

        diff = abs(guess - secret_number)

        if diff <= 5:
            distance_hint = "just few counts away from"
        elif diff <= 25:
            distance_hint = "tens away from"
        elif diff <= 50:
            distance_hint = "quite far from"
        else:
            distance_hint = "far more than 50 counts away from"

        print(f"Your guess is {direction} your secret number. Yoe are {distance_hint} the target.")
    
    guess = int(input("Guess again: "))

