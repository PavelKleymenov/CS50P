import sys, requests

"""Implement a program that returns the current cost for a specified amount of bitcoins"""
def main():
    print(f"${bitcoin_rate() * amount(sys.argv):,.4f}")


"""Implement a function that handles input"""
def amount(argv):

    # Set the amount to zero
    montant = 0

    # Render an error if users failed to provide number of bitcoins the want to query
    if len(argv) == 1:
        sys.exit("Missing command-line argument")

    # Render an error if users went overboard with CLA
    elif len(argv) > 2:
        sys.exit("Invalid Usage")

    # Othewise accept the number of bitcoins, rejecting an ivalid input down the line
    else:
        try:
            montant = float(argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    # Return the number of bitcoin
    return montant


"""Implement a function that returns bitcoin rate using CoinDesk Bitcoin Price Index API"""
def bitcoin_rate():
    rate = 0
    try:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = request.json()
        rate = response["bpi"]["USD"]["rate_float"]

    # Throw an error if something isn't right with the request
    except requests.RequestException:
        sys.exit("Bad Request")
    return rate