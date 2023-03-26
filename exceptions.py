# Example 1
# def add_vat(vat, prices):
#     """
#     Add commission to every price item in the provided iterable.
#
#     :param vat: float, vat percentage
#     :param prices: iterable, net prices as per customers' receipt
#     :return: list of prices with added vat
#     """
#     new_prices = [(price / 100 * vat) + price for price in prices]
#     return new_prices
#
# add_vat(vat=20, prices=[24, 0.15, '0', 32.45, 0])


# def apply_discount(product, discount):
#     """
#     Add a discount to the price.
#     :param product: dict obj, item spec including price
#     :param discount: float discount expressed in percent
#     :return: float new price
#     """
#     price = round(product['price'] * (1.0 - (discount / 100)), 2)
#     assert 0 <= price <= product['price']
#     return price
#
# #### VALID INPUT (comment / uncomment  to use as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 25 #(represents 25%)
# print(apply_discount(trainers, discount))
#
#
# #### INVALID INPUT (comment / uncomment to use  as necessary)###
# trainers = {'name': 'Running Trainers', 'price': 79.99}
# discount  = 200 #(represents 200%) --> Assertion Error will be raised
# print(apply_discount(trainers, discount))

# EXAMPLE 1 - try / except
#
# denominator = int(input("Please enter a number to divide by: "))
# try:
#     division_result = 100 / denominator
#     print(division_result)
#
# except ZeroDivisionError:
#     print("You cannot divide by 0, please try gain")

# EXAMPLE 2 -- raise exception

# number = int(input('Enter a number in the range 5-10: '))
#
# try:
#     if number < 5 or number > 10:
#         raise Exception
#
#     division_result = 100 / number
#     print(division_result)
#     print("Well Done")
#
# except:
#     print("Your number is NOT in the requested range")
#
#
# # EXAMPLE 3 - user defined errors
#
# class ValueIsBelowHundredError(ValueError):
#     """Raised when value is below 100"""
#     pass


# EXAMPLE 4 - debugging

# def debugging_n_breakpoints():
#     my_list = []
#     for i in range(10):
#         new_i = 10 + i
#
#         # import pdb
#         # pdb.set_trace()
#
#         print('new value is: ', i)
#         my_list.append((new_i))
#     return my_list
#
# debugging_n_breakpoints()

# CLASS PRACTICE

def age_validated(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    assert 12 < age <= 19

    return True

def name_validated(name_string):
    if ',' not in name_string:
        raise ValueError("Incorrect input: missing ',' to seperate name and surname")

    name, surname = name_string.split(',')

    if not len(name) or not len(surname):
        raise ValueError("Incorrect input: missing name or surname values")


#flag
isSuccessful = False

try:
    name= input("please enter your name and surname separated by comma: ")
    name_validated(name)
    age = int(input("Enter your age: "))
    age_validated(age)

except ValueError as exc:
    print("Invalid input: %s" % exc)

except AssertionError as exc:
    print("The age is not within the 'teenager' category")

else:
    with open("registration_file.txt", 'a+') as file:
        file.write("New member name: {} and age {}. \n".format(name, age))
        isSuccessful = True

finally:
    if isSuccessful:
        print("registration Process completed SUCCESSFULLY!")
    else:
        print("Could not complete registration. please try again.")

# INDEPENDENT CLASS PRACTICE

#
# def readFile(file_name):
#     try:
#         with open(file_name, 'r') as f:  # Open a file as read-only
#             print(f.readlines())
#
#     except FileNotFoundError as exc:
#         print(exc)
#
# readFile('registraton_file.txt')