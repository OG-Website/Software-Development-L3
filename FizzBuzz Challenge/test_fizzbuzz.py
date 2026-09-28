"""Automated tests for the FizzBuzz challenge."""

import unittest

from fizzbuzz import classify_number


class ClassifyNumberTests(unittest.TestCase):
    def test_fizzbuzz_for_multiple_of_three_and_five(self) -> None:
        self.assertEqual(classify_number(15), "fizzbuzz")

    def test_fizz_for_multiple_of_five_only(self) -> None:
        self.assertEqual(classify_number(10), "fizz")

    def test_buzz_for_multiple_of_three_only(self) -> None:
        self.assertEqual(classify_number(9), "buzz")

    def test_message_for_other_number(self) -> None:
        self.assertEqual(classify_number(7), "7 is not divisible by 3")

    def test_rejects_number_outside_range(self) -> None:
        with self.assertRaises(ValueError):
            classify_number(101)


if __name__ == "__main__":
    unittest.main()
