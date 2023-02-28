"""Implement a program that prompts the user for items,
    one per line, until the user inputs control-d"""
def main():

    # Call the function that's implemented below, when needed
    groceries()

    """Implement a function that outputs users
 grocery list in all uppercase, sorted alphabetically by item,
 prefixing each line with the number of times the user inputted that item"""
def groceries():

    # Create an empty grocery list
    grocery_list = {}

    # Run the code for as long as the code within the loop evaluates to True
    while True:

        """Try pass in the input value, adding to the total value of item
        if it's already in a grocery list, else adding an item tot the list"""
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1

            else:
                grocery_list[item] = 1

        # Once input function reaches the EOF, raise an appropriate exception
        except EOFError:

             """Print each item with the number of times it has been
                    added to the grocery list assigned to it"""
             for key, value in sorted(grocery_list.items()):
                print(value, key)

             # Snap out of the program when done counting
             break

# Invoke the main fucntion so as to get the program running
main()