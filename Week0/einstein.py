""" Implement a program in Python that prompts the user for mass
    and then outputs the equivalent number of Joules """
def main():

    # Get the input mass type - casting it along the way
    m = int(input("m: "))

    # Utilize the function created below to calculate the energy
    energy(m)

# Implenent a function that calculates energy via Einstein formula
def energy(m):
    E = int(m) * (300000000 ** 2)
    print(f"E: {E}")
    
# Invoke the main function so that the program actually works
main()