"""Implement a program that prompts the user for a fraction,
    formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer,
                how much fuel is in the tank"""

def main():

    # Prompt users with input
    prompt = input("Fraction: ")

    while True:

        try:
            # Ensure proper formatting
            above, beyond = prompt.split("/")

            # Define both parts of the fraction
            numerator = int(above)
            denominator = int(beyond)

            # Define the fraction itself
            fraction = numerator / denominator

            """If either parts turn out to be of non integer type,
            or division is skewed in some way, reprompt the user"""
            if fraction <= 1:
                break

        # Handle the exceptions, keeping on with a program even if those couldn't get resolved
        except(ValueError, ZeroDivisionError):
            pass

    # Define the total value of fuel
    fuel = round(float(fraction * 100))

    # Show what the gauge indicates based upon different possibilities
    if fuel <= 1:
        print("E")

    elif fuel >= 99:
        print("F")

    else:
        print (f"{fuel}%")

# Invoke the main fucntion so as to get the program running
main()
