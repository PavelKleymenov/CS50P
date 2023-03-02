"""Implement a program that prompts the user for a fraction,
    formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer,
                how much fuel is in the tank"""

def main():
    while True:
        try:
            # Prompt users with input
            prompt = input("Fraction: ")
            print (gauge(convert(prompt)))
            break

        # Handle the exceptions, keeping on with a program even if those couldn't get resolved
        except (ValueError, ZeroDivisionError):
            pass

# Show what the gauge indicates based upon different possibilities
def gauge(fuel):

    level = ""
    while True:

        if fuel <= 1:
            level = "E"

        elif 1 < fuel < 99:
            level = f"{round(fuel)}%"

        elif 99 <= fuel <= 100:
            level = ("F")

        else:
            raise ValueError

        break
    return level


def convert(prompt):

    # Ensure proper formatting
    above, beyond = prompt.split("/")

    # Define both parts of the fraction
    numerator = int(above)
    denominator = int(beyond)

    # Define the fraction itself
    fraction = numerator / denominator

    # Define the total value of fuel
    fuel = round(float(fraction * 100))
    return fuel

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()