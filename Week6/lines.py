import sys

"""Implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of
          code in that file, excluding comments and blank lines"""
def main():

     # If given valid CLA, print the total number of lines of code in that file
     if is_valid_argument(sys.argv):
          lines = read_lines(sys.argv[1])
          print(count_lines(lines))

     # Else if no file has been given, raise an exception
     else:
        raise FileNotFoundError

"""Implement a fuction that determines whether or not a provided file
                    meets all the requirements"""
def is_valid_argument(argv):

     # Render an error if user has provided less CLA's than needed
     if len(argv) < 2:
        sys.exit("Too few command-line arguments")

     # Render an error if user has provided too many CLA's
     elif len(argv) > 2:
          sys.exit("Too many command-line arguments")

     # Render an error if user is trying to provide a file with invalid extension
     elif ".py" not in argv[1]:
         sys.exit("Invalid extension")

     # Validate the input if all requirements have been met
     return True

"""Implement a function that returns a list containing each
     line in the provided Python file as a list item"""
def read_lines(valid_file):

    # Create an empty list that stores all the lines in a file
    lines = []

    # Open up the file for reading
    with open(valid_file, "r") as file:

          # Return a list with all the lines in a given file
          lines = file.readlines()
          return lines

"""Implement a function that determines how many lines of
               code are there in a given file"""
def count_lines(lines):

    # Set counter variable to zero
    count = 0

    # Iterate over each line in a file
    for line in lines:

        # Remove trailing whitespace from both sides
        line = line.strip()

        """Increment the total value of code lines in a file
        if a given line doesn't start with a hash symbol and
                    is not comprised of whitespaces"""
        if len(line) > 0:
            if not line.startswith("#"):
                count += 1


    # Return total value of lines in a given file
    return count

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()