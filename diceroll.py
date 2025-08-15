#dice roll
import random
rue = input("Roll a dice (y/n): ")
while True :
    if rue == "Y" or rue == "y" :
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print(f"Your roll is {roll1} & {roll2}")
        break

    elif rue == "N" or rue == "n" :
        print("Thanks for the roll")
        break
    else :
        print("invalid")
        break



