"""Implement a program that prompts the user for a string of text
and then outputs that same text but with all vowels omitted,
            whether inputted in uppercase or lowercase. """
def main():

    # Prompt user with input
    string = input("Your input: ")

    # Print out a new string wherein each vowel is missing
    print(omitted(string))

# Implement a function that purges strings of the vowels within it
def omitted(string):

    # Create a list containing all the vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Assign blank value to a corresponding variable
    no_vowels = ""

    # Iterate over the entire string inputted by the user
    for i in string:

        """Search for consonants in the string
    ensuring the removal of all case distinctions in a string. """
        if i.casefold() not in vowels:

            """Once a vowel is detected, mark one, as it were
                the total value of the words to be revised"""
            no_vowels += i
    return no_vowels


# Invoke the main function so that the program actually works
main()