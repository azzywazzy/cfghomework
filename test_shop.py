# import needed libraries
from unittest import TestCase, mock
from shop import *


# unit tests for item_choice_choice function
class TestItemChoice(TestCase):
    @mock.patch("shop.get_input", lambda _: "Console")
    def test_item_choice(self):
        self.assertEqual("Console", item_choice())


# unit tests for validate_choice function
class TestValidateChoice(TestCase):
    def test_x_equals_leave(self):
        result = validate_choice(choice="X")
        self.assertEqual("leaving", result)

    def test_m_equals_error(self):
        with self.assertRaises(ValueError):
            validate_choice("p")

    def test_console_is_valid(self):
        result = validate_choice(choice="Console")
        self.assertEqual("shopping", result)


# unit tests for check_budget function
class TestCanAfford(TestCase):
    def test_budget_enough(self):
        result = can_afford("Games", 100)
        self.assertTrue(result)

    def test_budget_not_enough(self):
        result = can_afford("Games", 50)
        self.assertFalse(result)


# unit tests for get price function
class TestGetPrice(TestCase):
    def test_get_price(self):
        result = get_price("Carry Case")
        self.assertEqual(15, result)


# unit tests for too many_attempts function
class TestTooMany(TestCase):
    def test_too_many(self):
        with self.assertRaises(TooManyAttempts):
            too_many_attempts(3)


if __name__ == "__main__":
    main()
