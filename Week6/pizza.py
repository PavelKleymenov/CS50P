import sys, csv
from tabulate import tabulate

"""Implement a program that expects exactly one command-line argument,
    the name (or path) of a CSV file in Pinocchio’s format, and
    outputs a table formatted as ASCII art using tabulate"""
def main():

    # If given valid CLA, return a table with all the menu item within it
    if is_valid(sys.argv):
        lines = read_lines(sys.argv[1])
        print(tabulate(lines[1::], lines[0], tablefmt="grid"))

    # Else if no file has been given, raise an exception
    else:
        raise FileNotFoundError

"""Implement a fuction that determines whether or not a provided file
                    meets all the requirements"""
def is_valid(argv):

    # Render an error if user has provided less CLA's than needed
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")

    # Render an error if user has provided too many CLA's
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")

    # Render an error if user is trying to provide a file with invalid extension
    elif ".csv" not in argv[1]:
        sys.exit("Invalid extension")

    # Validate the input if all requirements have been met
    return True

"""Implement a function that returns a table
        with all the contents of a CSV file within it"""
def read_lines(csvfile):

    # Create an empty table
    table = []

    # Open up the file for reading
    with open(sys.argv[1], "r") as csvfile:

            # Return a reader object
            reader = csv.reader(csvfile, delimiter=',')

            # Iterate over lines in a given CSV file
            for row in reader:
                table.append(row)

    # Return now populated table
    return table

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()