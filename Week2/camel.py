"""Implement a program that prompts the user for the name
        of a variable in camel case and outputs the
            corresponding name in snake case"""

# Prompt the user with input assuming it's in the camel case
def main():

    # Prompt the user with input assuming it's in the camel case
    camelCase = input("camelCase: ")

    # Use the function implemented below to case convert users input
    snake_case(camelCase)

def snake_case(camel):

    """Create a variable that as now stores an empty string in it,
            but will be used later on to keep track of each
                occurence of the camelCase in a given string"""
    snake = ""

    # Iterate through the entire string
    for i in range(len(camel)):
        if i != 0:

            """Replace an uppercase letter with an underscore followed by
                    the lowercase letter dividing the words comprising
                        the variable every time such case is detected"""
            if camel[i].isupper():
                snake += f"_{camel[i].lower()}"

                """Skip the current iteration of a for loop, so that control flow
                        of the program can begin the next one"""
                continue

            # Ensure that all the characters have been replace for real
        snake += camel[i]

    # Show what the variable name would be like in snake case
    print("Your variable in snake case is as follows:", snake)


# Invoke the main function so that the program actually works
main()