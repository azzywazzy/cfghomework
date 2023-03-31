# defining functions and classes

class TooManyAttempts(ValueError):
    """Raised when 3 or more attempts have been made"""
    pass


def get_input(message):
    return input(message)


def show_items():
    return {
        "Console": 200,
        "Games": 70,
        "Controller": 50,
        "Carry Case": 15
    }

def print_items():
    for key in show_items():
        print(key, " : £", show_items()[key])

def get_budget():
    budget = 100
    return budget


def welcome_customer():
    print("Welcome to the shop!")


def item_choice():
    choice = get_input("What would you like to buy? Choose from the items above or type 'x' to exit:  ")
    return choice


def validate_choice(choice):
    if choice in "xX":
        return "leaving"
    if choice in show_items():
        return "shopping"
    else:
        raise ValueError("Please choose one of the available items, or 'x' to exit")


def get_price(choice):
    return show_items()[choice]


def can_afford(choice, budget):
    if show_items()[choice] <= budget:
        return True
    else:
        return False


def attempt_purchase(choice, budget):
    if can_afford(choice, budget):
        print("Here's your {}!".format(choice))
        return True
    else:
        print("You cannot afford this")
        return False


def increment_attempts(attempts):
    attempts += 1
    return attempts


def continue_shopping():
    carry_on = input("Top up your balance by typing 'y' or type 'x' to exit:  ")
    return carry_on


def validate_continue(carry_on):
    if carry_on in "xX":
        return "leaving"
    elif carry_on in "yY":
        return "shopping"
    else:
        raise ValueError("Please choose 'y' to top up your balance, or 'x' to exit")


def add_funds(balance):
    extra = int(input("How much are you topping up your balance by?: "))
    new_balance = balance + extra
    return new_balance


def purchase_unsuccessful():
    print("Sorry your purchase wasn't successful. Please try again later.")


def too_many_attempts(attempts):
    if attempts == 3:
        raise TooManyAttempts
    else:
        return


def customer_leaving():
    print("Thank you for shopping with us. Please come again soon.")


def main():
    attempts = 0
    customer_funds = get_budget()

    try:
        get_budget()
        welcome_customer()
        print_items()
        choice = item_choice()
        customer_status = validate_choice(choice)

    except ValueError as exc:
        print("Invalid input: %s" % exc)

    else:
        while customer_status != "leaving":

            if attempt_purchase(choice, customer_funds):
                customer_status = "leaving"
                continue

            else:
                attempts = increment_attempts(attempts)

            if too_many_attempts(attempts):
                customer_status = "leaving"
                continue

            carry_on = continue_shopping()
            customer_status = validate_continue(carry_on)

            if customer_status == "leaving":
                continue

            customer_funds = add_funds(customer_funds)

    finally:
        customer_leaving()


if __name__ == "__main__":
    main()
