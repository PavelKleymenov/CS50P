"""Implement a program that enables a user to place an order,
prompting them for items, one per line, until the user inputs control-d"""
def main():

    # Call the function that's implemented below, when needed
    taqueria()

"""Implement a function that calculates the total value of an order"""
def taqueria():

    # Initiliaze a counter variable that's used to count order' total
    total = 0

    # Create a dictionary that holds all items that can be found in Felipe’s Taqueria
    valid_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    # Run the program for as long as the code within the loop evaluates to True
    while True:

        # Try to place an order ensuring it's in the titlecase
        try:
            item = input("Food item: ").title()

            """If an ordered item is in the menu, increment the order total,
            making sure it's formatted to two decimal points and has a dollar sign as prefix"""
            if item in valid_items:
                total += valid_items[item]
                print(f"${total:.2f}")

            """Skip the current iteration of the loop and the control flow
                    making program go to the next iteration"""
            continue

        # Raise exceptions when either input function has reached an EOF, or the user has typed an invalid item
        except (EOFError, KeyError):
            break

# Invoke the main fucntion so as to get the program running
main()