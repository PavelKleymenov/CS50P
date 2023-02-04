# Replace the strings with emojis using our own function
def main():

    #Get the input
    xyz = input(" ")

    # Get the output via our own function
    convert(xyz)

    # Output without passing the expected arguments
    convert()

# Create a function that replaces strings with emojis
def convert(xyz):
    print(xyz.replace(":)", "🙂").replace(":(","🙁"))

# Invoke the main function so that the program actually works
main()