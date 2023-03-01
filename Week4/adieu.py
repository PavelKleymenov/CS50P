import inflect
p = inflect.engine()

"""Implement a program that prompts the user for names,
one per line, until the user inputs control-d, assuming users
                provide at least one name"""
def main():

    # Call the function that's implemented below, when needed
    adieu()

"""Implement a function that takes users input and handles EOF exception"""
def adieu():

    # Create an empty list that will be populated with names, once those are given
    names = []

    # Try pass in the input, appending the list if all goes well
    try:
        while True:
            names.append(input("Input: "))

    # Print rendered string once program reaches the end of file
    except EOFError:
        print("\nAdieu, adieu, to", p.join(names))

# Invoke the main fucntion so as to get the program running
main()

