"""Implement a program that prompts the user to insert a coin,
    one at a time, each time informing the user of the amount due"""
def main():
    change_due()

def change_due():

    # Make sure that coke costs exactly 50 cents
    amount_due = 50

    # Create a list comprised of all the coins that can be accepted by a vending machine
    valid_coins = [5,10,25]

    # Do the code outlined within the loop for as long as there money to be inserted
    while amount_due > 0:

        # Make sure the customer knows how much he still needs to insert
        print(f"Amount Due: {amount_due}")

        # Prompt the customer with input
        coin = int(input("Insert Coin: "))

        """If the customer provided one of the authorized coins,
            decrement the amount due by the value of the coin
                        he/she's just inserted"""
        if coin in valid_coins:
            amount_due -= coin

        # Render an error message if the customer has tried to insert an unauthorized coin
        else:
            print(f"The coin is not valid: only {valid_coins} are up for insertion")

        """Once customer has inserted all the money needed to buy a coke
                         notify him/her about that"""
        if amount_due <= 0:
            print(f"Change Owed: {amount_due * -1}")


# Invoke the main function so that the program actually works
main()
