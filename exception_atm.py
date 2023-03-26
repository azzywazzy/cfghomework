def get_pin():
    inputted_pin = input("Please enter your PIN number: ")
    return inputted_pin


def valid_pin(pin_input):
    if pin_input != type(int):
        raise TypeError("Please only enter numbers")
    assert len(pin_input) == 4

    return True


def compare_pin(pin_try, pin):
    comparing_pins = True
    attempts = 0
    allowed_attempts = 3
    while comparing_pins:
        if pin_try == pin:
            print ("Thank you for entering your PIN")
            comparing_pins = False
        else:
            print("Invalid PIN entered. You have " + str(allowed_attempts - attempts) + " attempts remaining.")

        if attempts >= allowed_attempts:
            comparing_pins = False
            print("You've entered the wrong PIN {} times. Please contact your bank to unlock your account.".format(
                allowed_attempts))


def withdraw_cash(balance):

    try:
        request = int(input("How much would you like to withdraw?: "))


    if (balance-request) >= 0:
        print("Your current balance is {}.".format(balance-request))
    else:
        print("You don't have enough money.")




try:
    pin = get_pin()
    valid_pin(pin)

except