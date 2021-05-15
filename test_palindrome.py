import unittest
import palindrome

class TestCase(unittest.TestCase):

    def test_palindrome_1(self):
        self.assertEqual(palindrome.check_pal("Hello"), False)
    
    def test_palindrome_2(self):
        self.assertEqual(palindrome.check_pal("HellolleH"), True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
