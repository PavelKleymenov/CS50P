"""Implement a program that prompts the user for an input in English
    and then outputs the “emojized” version of that input, converting
    any codes (or aliases) therein to their corresponding emoji"""
import emoji
def main():

    # Call the function that's implemented below, when needed
    emojize()

"""Implement a function that does the conversion"""
def emojize():

    # Prompt users with input
    saisir = input()

    # Output the emojied input
    print(emoji.emojize(saisir))

# Invoke the main fucntion so as to get the program running
main()