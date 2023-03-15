import re

"""Implement a program that given an IP address as input,
validates or rejects that input based upon whether or not it
        matches a standardized pattern for IP adresses"""
def main():
    print(validate(input("IPv4 Address: ")))

"""Implement a function that determines whether or not
    an inputted IP meets the standardized criterion"""
def validate(ip):

    # Search for a pattern intrinsic to the IPv4 IP format
    if re.search(r"(\d{1,3}\.){3}", ip):

        # Iterate over entire IP address
        for octet in ip.split('.'):

            """Reject IP address either if octet exceeds
            the value of 255 or the number thereof transcends 5"""
            if int(octet) > 255 or len(ip.split('.')) > 4:
                return False

        # Otherwise validate IP address
        return True

    # Reject IP adress in case none of the requirements have been satisfied
    return False

# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()