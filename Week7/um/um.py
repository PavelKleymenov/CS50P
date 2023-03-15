import re

"""Implement a program that returns that total number of times distinct 'Um' appears in given string"""
def main():

    # Print the total number of 'Um' occurences
    print(count(input("Text: ")))

"""Implement a function that finds all instances of the 'Um' pattern within a string"""
def count(s):
    return len(re.findall(r"(^|\W)um($|\W)", s, flags = re.IGNORECASE))

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()