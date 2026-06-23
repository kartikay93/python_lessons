import random

print("WELCOME TO THE NUMBER GUESSING GAME!")

secret_number = random.randint(1, 100)

guess = int(input("Guess a number (1 - 100): "))
while True:
    print(f"You guessed: {guess}")
    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.\n")
        break
    
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number and abs(guess - secret_number) > 50:
        print("Your guess is too low and far from the secret number.")
    elif guess < secret_number and abs(guess - secret_number) > 25 and abs(guess - secret_number) <=50:
        print("Your guess is too low but close to the secret number.")
    elif guess < secret_number and abs(guess - secret_number) <= 25:
        print("Your guess is too low but very close to the secret number.")
    elif guess > secret_number and abs(guess - secret_number) > 50:
        print("Your guess is too high and far from the secret number.")
    elif guess > secret_number and abs(guess - secret_number) > 25 and abs(guess - secret_number) <=50:
        print("Your guess is too high but close to the secret number.")
    elif guess > secret_number and abs(guess - secret_number) <= 25:
        print("Your guess is too high but very close to the secret number.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    
    guess = int(input("Guess again: "))

