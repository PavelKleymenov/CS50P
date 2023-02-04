""" Implement a program that prompts the user for the name of a file \
                and then outputs that file's media type"""
def main():
    extensions()

# Implement a callable function
def extensions():

    # Prompt the user with input
    filename = input("File name: ").lower().strip().split(".")

    """Store every file type (per specification) in a dictionary
            so that it can be used later on to avoid repetition"""
    extension = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    """If provided input matches with any of the dictionary' key
        then display the value assigned to that key as output"""
    if filename[-1] in extension:
        print(extension[filename[-1]])

    # If there is no match, though, print out a common default type
    else:
        print("application/octet-stream")

        
# Invoke the main function so that the program actually works
main()