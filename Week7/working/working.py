import re

"""Implement a program that takes working hours in one format and converts it to another"""
def main():

    # Print expected input
    print(convert(input("Hours: ")))

"""Implement a function that does the format conversion"""
def convert(s):

    # Create a pattern for a regular expression
    pattern = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"

    # Check if specified pattern can be found within
    if match:= re.search(r"^" + pattern + " to " + pattern + "$", s):
        one_format = render(match.group(1), match.group(2), match.group(3))
        new_format = render(match.group(4), match.group(5), match.group(6))

        # If the pattern has been found return a newly formatted string
        return f"{one_format} to {new_format}"

    # Otherwise, if something wrong with the pattern, throw an error
    raise ValueError

"""Implement a function that facilitates rendition of a new format"""
def render(heurs, mins, format):

    # Consider different possibilities that ensure the proper rendition of working hours
    if heurs == "12":
        if format == "AM":
            hour = "00"
        else:
            hour = "12"

    else:
        if format == "AM":
            hour = f"{int(heurs):02}"
        else:
            hour = f"{int(heurs) + 12}"

    if mins == None:
        minute = "00"

    else:
        minute = f"{int(mins):02}"

    return f"{hour}:{minute}"

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()