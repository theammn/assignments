def count_characters(lines):
    return sum(len(line) for line in lines)

def count_words(lines):
    return sum(len(line.split()) for line in lines)

def count_lines(lines):
    return len(lines)
