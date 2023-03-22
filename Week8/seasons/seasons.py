from datetime import date
import sys, re, inflect

p = inflect.engine()

"""Implement a program that prompts the user for their date of birth
    in YYYY-MM-DD format and then sings prints how old they are in minutes,
    rounded to the nearest integer, using English words instead of numerals"""
def main():

    # Call the function that's implemented below, when needed
    get_age()

"""Implement a function that given the birthdate determines how old a person is"""
def get_age():

    # Prompt users for their birthdate
    birthdate = input("Date of Birth: ")

    # Try to enter a birthdate proceeding with the rest of the program if valid
    try:
        year, month, day = get_birthday(birthdate)

    # Otherwise abort the program
    except:
        sys.exit("Make sure you type in a valid birthdate. See the 'format' section for more informatiom")

    # Store the birthdate in a variable
    naissance = date(int(year), int(month), int(day))

    # Get at the current date
    now = date.today()

    # Calculate the difference between the two
    span = now - naissance

    # Calculate the total number of minutes a given user has lived so far
    minutes = span.days * 24 * 60

    # Format the input so as to show it in words
    output = p.number_to_words(minutes, andword='')

    # Spit the desired output back out
    print(f'{output.capitalize()} minutes')


"""Implement a function that ensures proper formatting of users' birthdate"""
def get_birthday(birthdate):

    # Validate users input if it matches regular expession below
    if re.search(r"^[\d]{4}-[\d]{2}-[\d]{2}$", birthdate):
        year, month, day = birthdate.split("-")
        return year, month, day

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()