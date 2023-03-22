from fpdf import FPDF

"""Implement a program that prompts the user for their name
and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf"""
class PDF(FPDF):

    # Create a method that specifies the outlook and position of the certificate title
    def header(self):

        # Set the image relative position
        self.image("shirtificate.png", 10, 65, 190, 190)

        # Style the inscription to your likinf
        self.set_font("helvetica", "I", 45)

        # Make sure the text aligned properly
        self.text(45, 45, "CS50 Shirtificate")

    # Create a method that specifies the outlook and position of the certificate holder within the shirt
    def footer(self):

        # Take care of styling font, it's coloring and the alignment to your liking
        self.set_font("helvetica", "B", 30)
        self.set_text_color(255,255,255)
        self.text(72, 140, txt =  f"{name} took CS50")

# Prompt users with input
name = input("What's your name? ")

# Create an object of above implemented class
pdf = PDF()

# Return desired certificate to it's requestee
pdf.add_page()
pdf.output("shirtificate.pdf")