"""Implement a program that prompts the user for a vanity plate
    and then outputs Valid if all of the requirements are met"""
def main():

    # Prompt users with desired plate name
    plate = input("Plate: ").strip()

    # Validate the request if all requirements are met
    if is_valid(plate):
        print("Valid")

    # Reject otherwise
    else:
        print("Invalid")

def is_valid(plate):

    # Slice the input from the 0th to the 2nd character
    start = plate[0:2]

    """Make sure plate' length stays within the range
                of two to six characters"""
    length = len(plate)
    if length < 2 or length > 6:
        return False


    # Make sure all characters are alphanumeric
    if not plate.isalnum():
        return False

    """Make sure all plates start with at least
                two letters"""
    if start.isdigit():
        return False

    # Make sure the first number in a string is not a zero
    i = 0
    while i < length:
        if not plate[i].isalpha():
            if plate[i] == "0":
                return False
            elif not plate[i:].isdigit():
                return False
            return True
        i += 1

    # Make sure numbers do not come in the middle of the plate
    for i in range(length):
        if plate[i].isdigit():
            if not plate[i:].isdigit():
                return False

    # If all conditions are met, validate the plate
    return True

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()