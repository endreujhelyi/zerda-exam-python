import unittest
import third

class TestCountLetterInString(unittest.TestCase):

    def test_is_number_of_letter_ok(self):
        self.assertEqual(third.count_letter_in_string("hello", "l"), 2)

    def test_first_input_not_string(self):
        self.assertEqual(third.count_letter_in_string("szuperhello", 1), 0)

    def test_second_input_not_string(self):
        self.assertEqual(third.count_letter_in_string([1, 2, 3], "x"), 0)


if __name__ == '__main__':
    unittest.main()
