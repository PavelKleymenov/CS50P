from validator_collection import checkers

"""Implement a program that checks whether or not users have valid email address"""
def main():
    print(validate(input("What's your email address: ")))

"""Implement a function that determines whether or not
        given email address meets all requirements"""
def validate(email):
    return 'Valid' if checkers.is_email(email) == True else 'Invalid'


# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()
