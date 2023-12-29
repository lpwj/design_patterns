from typing import Dict, Callable

# dictionary we do not have access to change. It creates the type of factories. Creator Dictionary
payment_methods: Dict[str, Callable[[float], None]] = {
    "CreditCard": lambda amount: print(
        f"Pay {amount} with credit card (Functional Factory)"
    ),
    "DebitCard": lambda amount: print(
        f"Pay {amount} with debit card (Functional Factory)"
    ),
    "PayPal": lambda amount: print(f"Pay {amount} with PayPal (Functional Factory)"),
    "Cash": lambda amount: print(f"Pay {amount} with cash (Functional Factory)"),
}


def factoryContext(type: str):
    """Creates the given type of factory.

    Args:
        type (str): Factory type to use.
        amount (float): The amount to pay.

    Returns:
        Callable[[float], None]: The Factory callable function object to execute.
    """
    # Creating the factory
    return payment_methods[type]


def pay(factory: Callable[[float], None], amount: float) -> None:
    factory(amount)


# Example usage
context_credit_card = factoryContext("CreditCard")
context_debit_card = factoryContext("DebitCard")
context_paypal = factoryContext("PayPal")
context_cash = factoryContext("Cash")


pay(context_credit_card, 100)  # Pay 100 with credit card
pay(context_debit_card, 200)  # Pay 200 with debit card
pay(context_paypal, 300)  # Pay 300 with PayPal
pay(context_cash, 400)  # Pay 400 with cash
