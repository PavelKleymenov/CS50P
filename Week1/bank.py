"""Implement a program that prompts the user for a greeting,
   bringing in him a certain amount of money depending on the response given"""
greeting = input("What's the greeting?")

answer = greeting.lower().strip()

if answer.startswith("hello"):
    print("$0")

elif answer.startswith("h"):
    print("$20")
    
else:
    print("$100")