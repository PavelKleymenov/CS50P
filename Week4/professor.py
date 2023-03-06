import random

"""Implement a program that simulates arithmetic exercise of three difficulty levels"""
def main():

    # Set the initial value of score to zero
    score = 0

    # Generate a difficulty level for a game
    level = get_level()

    # Run ten iterations of a problem
    for _ in range(10):

        # Prompt user with addends
        x = generate_integer(level)
        y = generate_integer(level)

        # Store the value of addition in a variable representing expected output
        output = x + y

        # Prompt users with expected input equation
        print(f"{x} + {y} = ")

        # Make sure the program exits out if user has made more than three attempts for a given problem
        for i in range(3):
            try:

                # If the problem has been solved correctly, update the score
                answer = int(input())
                if answer == output:
                    score += 1
                    break

                    """If the wrong answer has been given, reprompt the user first,
                    and then after three unsuccessful tries give the right answer"""
                else:
                    print("EEE")
                    print(f"{x} + {y} = ")
                    if i == 2:
                        print(f"Answer: {output}")
                        break

            # Throw an error in case users provide invalid answer
            except ValueError:
                pass

    # Display the total score
    print(f"Score: {score}")

"""Implement a function that ensures valid input"""
def get_level():

    level = input("Level: ")

    # Reprompt users in case any of the conditions below haven't been satisfied
    if level.isalpha() or int(level) <= 0 or int(level) > 3:
        input("Level: ")
    else:
        level = int(level)
        if level in [1,2,3]:
            return level

"""Implement a function that ensures proper numbers for each difficulty level"""
def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0,9)
        elif level == 2:
            return random.randint(10,99)
        elif level == 3:
            return random.randint(100,999)

    # Throw an exception in case users provide invalid input
    except ValueError:
        pass

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()