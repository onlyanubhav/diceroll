import random



while True:
    computer_chose = random.randint(1,3)

    user_chose = input("Rock, Paper or Scissors? (r/p/s): ")
    if computer_chose == 1 :
        # Rock
        if user_chose == "R" or user_chose == "r" :
            print("Tie breaker!!! \nComputer Chose Rock too")
        elif user_chose == "P" or user_chose == "p" :
            print("You win!!!\nComputer Chose Rock")
        elif user_chose == "S" or user_chose == "s" :
            print("You lost \nComputer Chose Rock")
        else:
            print("invalid")
    elif computer_chose == 2 :
        # Paper
        if user_chose == "R" or user_chose == "r" :
            print("You win!!! \nComputer Chose Paper")
        elif user_chose == "P" or user_chose == "p" :
            print("Tie breaker!!! \nComputer Chose Paper too")
        elif user_chose == "S" or user_chose == "s" :
            print("You lost \nComputer Chose Paper")
        else:
            print("invalid")
    elif computer_chose == 3 :
        # Scissors
        if user_chose == "R" or user_chose == "r" :
            print("You win!!! \nComputer Chose Scissors")
        elif user_chose == "P" or user_chose == "p" :
            print("You lost \nComputer Chose Scissors")
        elif user_chose == "s" or user_chose == "S" :
            print("Tie breaker!!! \nComputer Chose scissors too")
        else:
            print("invalid")
    else:
        print("invalid")
    break
