"""Implement a program that prompts the user for a time '
and outputs whether it's breakfast time, lunch time, or dinner time"""
def main():

    # Prompt the user with the input
    time = input("What time is it? ")

    """Invoke the convert function so that the program can read
            the input content in a desired format"""
    mealtime = convert(time)

    """Run througn all the possible meal times
    so that you can determine which meal should be eaten"""
    if mealtime >= 7 and mealtime <= 8:
        print("breakfast time")

    elif mealtime >= 12 and mealtime <= 13:
        print("lunch time")
        
    elif mealtime >= 18 and mealtime <= 19:
        print("dinner time")

""" Implement a function that converts time
to the corresponding number of hours as a float."""
def convert(time):

    """Make sure the colon between value of hours and
            that of minutes is treated as value, too"""
    time = time.split(":")

    # Type cast the minutes value making it a float
    minutes = float(time[1]) / 60
    return(float(time[0]) + minutes)

if __name__ == "__main__":
    main()