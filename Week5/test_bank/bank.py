"""Implement a program that prompts the user for a greeting,
that will determine how many dollars one such user will have received"""
def main():

    # Prompt users with input
    text = input()
    greeting = value(text)
    return greeting

"""Implement a function that returns the number of dollars to be received"""
def value(greeting):

     # Prompt users with a greeting
     greeting = greeting.strip().casefold()

     # Consider various possibilities
     if greeting.startswith("hello"):
         return 0

     elif greeting[0] == "h":
          return 20

     else:
        return 100

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()