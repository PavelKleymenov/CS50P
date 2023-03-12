import sys, csv

"""Implement a program that given a CSV file outputs
        a new one with a more user friendly format"""
def main():

    # If users provide valid input, format the initial CSV file
    if is_valid(sys.argv):
        convert_csv(sys.argv[1], sys.argv[2])

    # If though, no file has been provided, throw an error
    else:
        raise FileNotFoundError

"""Implement a function that determines whether or not
        an input given by users is valid"""
def is_valid(argv):


    # Render an error if user has provided less CLA's than needed
    if len(argv) < 3:
        sys.exit('Too few command-line arguments')

    # Render an error if user has provided too many CLA's
    elif len(argv) > 3:
        sys.exit('Too many command-line arguments')

    # Render an error if user is trying to provide a file with invalid extension
    elif '.csv' not in argv[1]:
        sys.exit('Invalid extension')

    # Validate the input if all requirements have been met
    return True


"""Implement a function that load a new formatted file into a memory"""
def convert_csv(before, after):

    # Open up the initial file for reading
    with open(before, 'r') as csvfile:

            """Map the information in each row to a dictionary whose keys
                    are given by the optional fieldnames parameter"""
            reader = csv.DictReader(csvfile)

            # Write the newly created file into a memory
            with open(after, 'w') as modified:

                # Map dictionaries onto output rows, setting desired fieldnames
                writer = csv.DictWriter(modified, fieldnames=['first','last', 'house'])

                # Add a header to the newly created file
                writer.writeheader()

                # Iterate over rows in the file, giving them proper format
                for row in reader:
                    name = row['name'].replace('"', '').split(',')
                    writer.writerow({'first': name[1].strip(), 'last': name[0].strip(), 'house': row['house'].strip()})

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()