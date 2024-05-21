# test_file_utils.py
import unittest
from file_utils import count_characters, count_words, count_lines, file_statistics

class TestUtils(unittest.TestCase):
    def test_count_characters(self):
        self.assertEqual(count_characters(["hello\n", "world\n"]), 11)

    def test_count_words(self):
        self.assertEqual(count_words(["hello world\n", "test\n"]), 3)

    def test_count_lines(self):
        self.assertEqual(count_lines(["hello\n", "world\n", "test\n"]), 3)

    def test_file_statistics(self):
        # You need to create an actual file or mock reading a file for this test
        pass

if __name__ == '__main__':
    unittest.main()

