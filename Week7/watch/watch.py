import re

"""Implement a function called parse that expects a string of HTML as input,
extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
        and returns its shorter, shareable youtu.be equivalent as a str"""
def main():

    # Print expected output
    print(parse(input("HTML: ")))

"""Implement a function that searches for a particular pattern and then returns it"""
def parse(s):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-z0-9]+)\"></iframe>", s, re.IGNORECASE):
        return f"https://youtu.be/{link.group(2)}"

    # If the input does not contain any such URL at all, return None
    return None


# Invoke the main fucntion so as to get the program running
if __name__ == "__main__":
    main()