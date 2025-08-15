
import random

number_to_guess = random.randint(1, 100)

while True:
        guess = int(input("Enter a number between 1 to 100: "))

        if guess > number_to_guess:
            print("too high")
        elif guess < number_to_guess:
            print("too low")
        else:
            print("Right!")
            break

