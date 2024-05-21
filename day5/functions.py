def functions(text):
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

