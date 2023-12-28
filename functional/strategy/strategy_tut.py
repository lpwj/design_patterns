# Strategy pattern in Python using functional programming for the payment example


# A generic function that takes a function and an amount as arguments
# and calls the function with the amount
def pay(func, amount):
    func(amount)


# Some concrete functions that represent different payment methods
def credit_card(amount):
    print(f"Pay {amount} with credit card")


def debit_card(amount):
    print(f"Pay {amount} with debit card")


def pay_pal(amount):
    print(f"Pay {amount} with PayPal")


def cash(amount):
    print(f"Pay {amount} with cash")


# Example usage
pay(credit_card, 100)  # Pay 100 with credit card
pay(debit_card, 200)  # Pay 200 with debit card
pay(pay_pal, 300)  # Pay 300 with PayPal
pay(cash, 400)  # Pay 400 with cash
