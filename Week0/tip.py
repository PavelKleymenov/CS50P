"""Implement a function that calculates how much should be left as a tip"""
def main():

    # Prompt the user for input both for the amount of money and the percent
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Prompt with the formula to calculate the tip 
    tip = dollars * percent

    # Print out a formatted string that tells how much is the tip
    print(f"Leave ${tip:.2f}")

"""Implement a function that typecasts the dollars and removes the dollar sign from the output"""
def dollars_to_float(d):
    d = d.replace("$"," ")
    return float(d)

"""Implement a function that typecasts the percent and outputs its value as a decimal"""
def percent_to_float(p):
    p = p.replace("%"," ")
    p = float(p)
    p = p / 100
    return p

# Invoke the main function so that the program actually works
main()