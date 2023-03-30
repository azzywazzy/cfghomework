# import needed libraries
from unittest import TestCase, main, mock

# unit tests for item_choice_choice function
from shop import item_choice
class TestItemChoice(TestCase):
    @mock.patch("shop.get_input", lambda _: "Console")
    def test_item_choice(self):
        self.assertEquals("Console", item_choice())

# unit tests for validate_choice function
from shop import validate_choice
class TestValidateChoice(TestCase):
    def test_x_equals_leave(self):
        result = validate_choice(choice="X")
        self.assertIsNone(result)
    def test_m_equals_error(self):
        with self.assertRaises(ValueError):
            validate_choice("p")
    def test_console_is_valid(self):
        result = validate_choice(choice="Console")
        self.assertEquals("Console", result)

# unit tests for check_budget function
from shop import check_budget
class TestBudgetCheck(TestCase):
    def test_is_enough(self):
        result = check_budget(100,20)
        self.assertTrue(result)
    def test_is_not_enough(self):
        result = check_budget(100,200)
        self.assertFalse(result)

# unit tests for attempt_purchase function
from shop import attempt_purchase
class TestAttempts(TestCase):
    def test_attempts_itr(self):
        result = attempt_purchase(False, 1)
        self.assert_(result == 2)

# unit tests for toomany_attempts functionx
from shop import toomany_attempts
from shop import TooManyAttempts
class TestTooMany(TestCase):
    def test_too_many(self):
        with self.assertRaises(TooManyAttempts):
            toomany_attempts(3)





if __name__ == "__main__":
    main()
