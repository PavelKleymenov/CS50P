"""implement a program that prompts users to input a fruit (case-insensitively)
        and then outputs the number of calories in one portion of that fruit,
                per the FDA's poster for fruits"""
def main():
    # Prompt users with input
    fruit = input("Item: ").casefold()

    # Use the function implemented below to handle the input
    nutrition_facts(fruit)

def nutrition_facts(fruit):

    # Create a dictionary that represents the FDA spreadsheet
    calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineaple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    """If user' input matches with one of the elements in the dictionary,
            display the calories assosiated with that element"""
    if fruit in calories:
        print(f"Calories: {calories[fruit]}")


# Invoke the main function so that the program actually works
main()