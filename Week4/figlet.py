import sys, random
from pyfiglet import Figlet
figlet = Figlet()

"""Implement a program that makes large letters, ASCII style, out of ordinary text"""
def main(argv):

    # If users provided valid CL input, render converted text
    if font(argv):
        message()

    # Render an apology if users failedd to use the program properly
    else:
        sys.exit("Invalid usage")


"""Implement a function that selects random font"""
def font(argv):

    # Get a list of avaliable fonts
    font_list = figlet.getFonts()
    is_font_set = False

    # If users provided exactly one CLA, pick a font out of a random family
    if len(argv) == 1:
        figlet.setFont(font = font_list[random.randint(0, 250)])
        is_font_set = True

    # Render a newly styled input if all of the requirements are met
    elif len(argv) == 3:
        if argv[1] == "-f" or argv[1] == "--font":
            if argv[2] in font_list:
                figlet.setFont(font = argv[2])
                is_font_set = True

    return is_font_set

"""Implement a function that takes an input and returns ASCII'd rendition of that input"""
def message():
    usage = input("Input: ")
    print("Output:", figlet.renderText(usage), sep="\n")

# Invoke the main fucntion so as to get the program running
main(sys.argv)