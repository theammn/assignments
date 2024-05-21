def count_characters(lines):
    return sum(len(line) for line in lines)

def count_words(lines):
    return sum(len(line.split()) for line in lines)

def count_lines(lines):
    return len(lines)

def file_statistics(filename):
    try:
        with open(filename, 'r') as file:
            num_characters = num_lines = num_words = 0
            for line in file:
                num_lines += 1
                num_characters += len(line)
                num_words += len(line.split())
        return num_characters, num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return -1, -1, -1
