"""Implement a program that prompts the user
for a date, anno Domini, in month-day-year order,"""
def main():

    # Call the function that's implemented below, when needed
    anno_domini()

"""Implement a function that, given an input, prints out a hyphen
separated time periods, while also formatted to having leading zeroes"""
def anno_domini():

    # Create a list of all months that are known to make up a year
    months = [ "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # Set initial value of each time period to an empty string
    month = day = year = ""

    # Run the code within the block for as long as the code within the loop evaluates to True
    while True:

        # Prompt users with input, removing all the trailing whitespaces
        date = input("Date: ").strip()

        # Consider different possibilities
        if "/" in date:
            month, day, year = date.split("/")

        elif "," in date:
            month, day, year = date.replace(",", "").split()
            if month in months:
                month = months.index(month) + 1

        # Skip the current iteration of the program
        else:
            continue

        # Handle exceptions
        try:
            day = int(day)
            year = int(year)
            month = int(month)
            if day > 31 or month > 12:
                continue

        # Break out of the program if user has provided invalid input
        except ValueError:
            continue
        break

    # Print out results in a required format
    print(f"{year}-{month:02}-{day:02}")

# Invoke the main fucntion so as to get the program running
main()