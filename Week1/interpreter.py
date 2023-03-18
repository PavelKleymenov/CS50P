"""Implement a program that prompts the user for an arithmetic expression
    and then calculates and outputs the result as a floating-point value
                    formatted to one decimal place"""
def main():
    interpreter()

def interpreter():
    """Prompt the user with the input making sure the string is separated into
        a sequence of values each of which can be assigned to its own variable"""
    x,y,z = input("Expression: ").split()

    # Type cast the X and Z variables so that the output is of the float type
    x = float(x)
    z = float(z)

    """Run through all four arithmetic operation
        ensuring the output is a floating - point value
        formatted to one decimal point"""
    if y == "+":
        print(f"{x+z:.1f}")

    elif y == "-":
        print(f"{x-z:.1f}")

    elif y == "*":
        print(f"{x*z:.1f}")

    elif y == "/":
        print(f"{x/z:.1f}")
        
        
# Invoke the main function so that the program actually works
main()