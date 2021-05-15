import unittest
import word_count

class TesetCase(unittest.TestCase):

    def test_word_count_1(self):
        self.assertEqual(word_count.word_count("Hello, this is the test case"), 6)

    def test_word_count_2(self):
        self.assertEqual(word_count.word_count(""), 0)

    def test_word_count_3(self):
        self.assertEqual(word_count.word_count(" "), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)