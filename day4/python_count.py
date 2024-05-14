#How many characters does the file have.
#How many lines are in the file.
#How many words are in the file. (For our purpose you can assume that any two things separated by spaces are separate words.

import sys

def file_statistics(text):
    """Function to compute characters, lines, and words from the given file."""
    try:
        with open(text, 'r') as file:
            num_characters = num_lines = num_words = 0
            for line in file:
                num_lines += 1
                num_characters += len(line)
                num_words += len(line.split())
        return num_characters, num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {text}")
        return -1, -1, -1

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py text")
        sys.exit(1)

    file = sys.argv[1]
    num_characters, num_lines, num_words = file_statistics(file)

    if num_characters != -1:
        print(f"The file has {num_characters} characters")
        print(f"The file has {num_lines} lines")
        print(f"The file has {num_words} words")
main()
