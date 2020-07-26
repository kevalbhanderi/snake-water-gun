import random

print("\t \t snake water gun game \n")

chance = 5
no_of_chance = 0
human_point = 0
computer_point = 0
lst = ['s', 'w', 'g']

while no_of_chance < chance:
    user_inp = input(f"Choose Snake,Water,Gun {lst} : ")
    random_inp = random.choice(lst)


    if user_inp == "s" and random_inp == "g":
        computer_point = computer_point + 1
        print(f"computer choose {random_inp}")
        print("Computer win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "s" and random_inp == "w":
        human_point = human_point + 1
        print(f"you win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "s" and random_inp == "s":
        print("same input")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "g" and random_inp == "s":
        human_point = human_point + 1
        print("you win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "g" and random_inp == "w":
        computer_point = computer_point + 1
        print(f"computer choose {random_inp}")
        print("computer win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "g" and random_inp == "g":
        print("same input")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "w" and random_inp == "s":
        computer_point = computer_point + 1
        print(f"computer choose {random_inp}")
        print("computer win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "w" and random_inp == "g":
        human_point = human_point + 1
        print("you win 1 point")
        print(f"computer point is {computer_point} and your point is {human_point}")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    elif user_inp == "w" and random_inp == "w":
        print("same input")
        print(f"computer point is {computer_point} and your point is {human_point} \n")

        if user_inp == random_inp:
            no_of_chance = no_of_chance
            print(f"{chance - no_of_chance} is left out of {chance} \n")
        else:
            no_of_chance = no_of_chance + 1
            print(f"{chance - no_of_chance} is left out of {chance} \n")

    else:
        if user_inp != "s" or "w" or "g":
            print("Wrong Input !! TRY AGAIN")


print("Game Over")

print(f"computer point is {computer_point} and your point is {human_point}")
if computer_point > human_point:
    print("Computer is win")

if computer_point < human_point:
    print("You are win")

if computer_point == human_point:
    print("Match is Tie")
