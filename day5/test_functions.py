import pytest
from functions import count_characters, count_words, count_lines, file_statistics

def test_count_characters():
    # Test counting characters including newlines
    assert count_characters(["hello\n", "world\n"]) == 12

    # Alternatively, handle different newline conventions
    stripped_lines = [line.rstrip('\n') for line in ["hello\n", "world\n"]]
    assert count_characters(stripped_lines) == 10

def test_count_words():
    assert count_words(["hello world\n", "test\n"]) == 3

def test_count_lines():
    assert count_lines(["hello\n", "world\n", "test\n"]) == 3

def test_file_statistics(tmp_path):
    # Create a temporary file
    file_content = "hello world\nthis is a test\n"
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(file_content)

    num_characters, num_lines, num_words = file_statistics(test_file)

    assert num_characters == len(file_content)
    assert num_lines == 2
    assert num_words == 5

if __name__ == '__main__':
    pytest.main()
