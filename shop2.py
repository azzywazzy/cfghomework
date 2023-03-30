# defining functions and classes

class TooManyAttempts(ValueError):
    """Raised when 3 or more attempts have been made"""
    pass

def get_input(message):
    return input(message)


def item_choice():
    choice = get_input("What would you like to buy? Or type 'x' to exit:  ")
    return choice


def validate_choice(choice):
    if choice in "xX":
        global customer_left
        customer_left = True
        return
    if choice in items():
        return choice
    else:
        raise ValueError("Please choose one of the available items, or 'x' to exit")


def check_budget(budget, price):
    if price <= budget:
        return True
    else:
        return False


def attempt_purchase(can_afford,attempts):
    if can_afford:
        print("Here's your {}!".format(choice))
        global customer_left
        customer_left = True
    else:
        attempts += 1
        print("You cannot afford this.")
        return attempts


def continue_shopping():
    carry_on = input("Top up your balance by typing 'y' or type 'x' to exit:  ")
    return carry_on


def validate_continue(carry_on):
    if carry_on in "xX":
        global customer_left
        customer_left = True
        return
    if carry_on in "yY":
        return
    else:
        raise ValueError("Please choose 'y' to top up your balance, or 'x' to exit")


def add_funds(balance):
    extra = int(input("How much are you topping up your balance by?: "))
    new_balance = balance + extra
    return new_balance


def toomany_attempts(attempts):
    if attempts == 3:
        raise TooManyAttempts
    else:
        return

def items():
    return {
        "Console": 200,
        "Games": 70,
        "Controller": 50,
        "Carry Case": 15
    }

def main():

# end of functions and classes

    # start of program
    # items = {
    #     "Console": 200,
    #     "Games": 70,
    #     "Controller": 50,
    #     "Carry Case": 15
    # }

    # initialising variables
    customer_funds = 100
    customer_left = False
    attempts = 0

    # shopping loop
    try:
        print("Welcome to the shop. Browse our items, or press 'x' to exit.")
        print(items())

        choice = item_choice()
        validate_choice(choice)

    except ValueError as exc:
        print("Invalid input: %s" %exc)

    else:
        while not customer_left:

            attempts = attempt_purchase(check_budget(customer_funds, items()[choice]), attempts)
            toomany_attempts(attempts)

            if customer_left:
                continue

            carry_on = continue_shopping()
            validate_continue(carry_on)

            if customer_left:
                continue

            customer_funds = add_funds(customer_funds)

    finally:
        if customer_left:
            print("Thank you for shopping with us. Please come again soon.")
        else:
            print("Sorry your purchase wasn't successful. Please try again later.")

if __name__ == "__main__":
    main()