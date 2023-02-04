"""Implement a program that prompts the user for a vanity plate
    and then outputs Valid if all of the requirements are met"""
import re
def main():

    # Prompt users with desired plate name
    plate = input("Plate: ").strip()

    # Validate the request if all requirements are met
    if is_valid(plate):
        print("Valid")

    # Reject othrwise
    else:
        print("Invalid")

def is_valid(plate):

    start = plate[0:2]
    middle = plate[len(plate)//2]
    end = plate[-1]
    """Make sure plate' length stays within the range
                of two to six characters"""
    length = len(plate)

    # Make sure the input is within the range of 2 to 6 characters
    if length >= 2 and length <= 6:
        if start.isalpha():
            if plate.isalnum():
                if middle.isdigit() and end.isdigit():
                    if plate.startswith("0", 3) and end.isalpha():
                        return True
    else:
        return False
main()