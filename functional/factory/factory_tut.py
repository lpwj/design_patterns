# Factory pattern in Python using functional programming for the payment example

# A dictionary that maps different types to different functions that create payment methods
payment_methods = {
    "CreditCard": lambda amount: print(f"Pay {amount} with credit card"),
    "DebitCard": lambda amount: print(f"Pay {amount} with debit card"),
    "PayPal": lambda amount: print(f"Pay {amount} with PayPal"),
    "Cash": lambda amount: print(f"Pay {amount} with cash"),
}


# A generic function that takes a type and an amount
# and calls the corresponding function from the dictionary with the amount
def pay(type, amount):
    payment_methods[type](amount)


# Example usage
pay("CreditCard", 100)  # Pay 100 with credit card
pay("DebitCard", 200)  # Pay 200 with debit card
pay("PayPal", 300)  # Pay 300 with PayPal
pay("Cash", 400)  # Pay 400 with cash
