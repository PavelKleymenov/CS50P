мmport sys
from os.path import splitext
from PIL import Image, ImageOps


"""Implement a program thayt given images overlays them with another picture"""
def main():

    # If given valid input, overlay the images
    if is_valid(sys.argv):
        overlay(sys.argv[1], sys.argv[2])

    # If though, no file has been provided, throw an error
    else:
        raise FileNotFoundError

"""Implement a function that determines whether or not
        an input given by users is valid"""
def is_valid(argv):

    # Render an error if user has provided less CLA's than needed
    if len(argv) < 3:
        sys.exit('Too few command-line arguments')

    # Render an error if user has provided too many CLA's
    elif len(argv) > 3:
        sys.exit('Too many command-line arguments')


    # Create a list comprised of supported file extensions
    valid_extensions = ['.jpeg', '.jpg', '.png']

    # Determine file extension of both the input and the output
    before = splitext(argv[1])
    after = splitext(argv[2])

    # Exit a program if users provide file with an invalid extension
    if before[1].casefold() and after[1].casefold() not in valid_extensions:
        sys.exit('Not a valid file extension')

    # Exit a program if the input’s name does not have the same extension as the output’s name
    if before[1].casefold() != after[1].casefold():
        sys.exit('Extensions do not match')

    # Validate the input if all requirements have been met
    return True

"""Implement a program that does the overlay effect """
def overlay(input, output):
    try:

        # Open the input image
        with Image.open('shirt.png', 'r') as shirt:
                with Image.open(input) as undergraduate:

                    # Resize and crop the input
                    undergraduate = ImageOps.fit(undergraduate, shirt.size, bleed=0.0, centering=(0.5, 0.5))

                    # Overlay the body of a puppet with a shirt
                    undergraduate.paste(shirt, shirt)

                    # Save the overlayed image
                    undergraduate.save(output)

    # Otherwise, OS specific function returns a system-related error
    except OSError:
        sys.exit(f'Unable to overlay {input}')


# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()