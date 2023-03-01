import random

"""Implement a program that allows users to guess numbers"""
def main():

    # Call the function that's implemented below, when needed
    nombre(saisir())

"""Implement a function that ensures that input is valid"""
def saisir():

    level = 0

    """Run the code within the block for as long as the
        condition within the loop evaluates to True"""
    while True:

        # Raise an exception if users provide invalid input
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            break
        except ValueError:
            continue
    return level

"""Implement a function that facilitates guessing"""
def nombre(level):

    # Get a random number from within the range of 1 up to the number provided by the user
    number = random.randint(1, level)
    guess = 0

    # Consider different possibilities
    while guess != number:
        try:

            # Prompt users with input
            guess = int(input("Guess: "))

            if guess == number:
                print("Just Right!")
                break

            elif guess < number:
                print("Too small!")

            else:
                print("Too Large!")

        except ValueError:
            continue
        
# Invoke the main fucntion so as to get the program running
main()