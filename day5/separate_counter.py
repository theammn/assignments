# file_utils.py
def file_statistics(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_characters = count_characters(lines)
            num_lines = count_lines(lines)
            num_words = count_words(lines)
        return num_characters, num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return -1, -1, -1

