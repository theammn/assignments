import sys
from file_utils import file_statistics

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py text")
        sys.exit(1)

    file_path = sys.argv[1]
    num_characters, num_lines, num_words = file_statistics(file_path)

    if num_characters != -1:
        print(f"The file has {num_characters} characters")
        print(f"The file has {num_lines} lines")
        print(f"The file has {num_words} words")

if __name__ == '__main__':
    main()
