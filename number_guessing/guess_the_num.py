import random

random_num = random.randint(1, 10)

# instructions
print("Guess the number between 1-10\n"
      "you have 3 attempts\n")

# attempt count variable
attempts = 2

# if attempt is eligible, it will give the user chances to play the game
while attempts > 0 or attempts == 0:
    # takes the input from user
    # as we will take string and int both type:
    # we did not use int() in user_input
    user_input = input("Guess the Number: ")

    # try's if the conditions are working with error, if not it will pass to the "except" in below
    try:

        # if the user guesses the number he won!
        if int(user_input) == random_num:
            print("you won the game!")
            print(f"the number was {random_num}!")
            break

        # if the user did not guess the number in this attempt
        elif int(user_input) != random_num:
            # minus one attempt, the user had used
            attempts -= 1
            # return user was not correct
            print("it was not the number")
            # return how many attempts he left
            print(f"you have {attempts + 1} attempts left")


    # if the "try" condition returns error cause of user's input the "except" will return and error message
    except:
        # return error of user's input was something else
        print("Error, guess number with 1,2,3 etc")
