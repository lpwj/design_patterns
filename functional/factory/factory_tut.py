"""Module with the factory pattern. (Functional programming)"""

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


def factory_context(payment_type: str):
    """Creates the given type of factory.

    Args:
        type (str): Factory type to use.
        amount (float): The amount to pay.

    Returns:
        Callable[[float], None]: The Factory callable function object to execute.
    """
    # Creating the factory
    return payment_methods[payment_type]


def pay(factory: Callable[[float], None], amount: float) -> None:
    """Executes the action of paying according to the factory function received.

    Args:
        factory (Callable[[float], None]): The factory to to use.
        amount (float): The amount to pay with the factory outcome.
    """
    factory(amount)


# Example usage
context_credit_card = factory_context("CreditCard")
context_debit_card = factory_context("DebitCard")
context_paypal = factory_context("PayPal")
context_cash = factory_context("Cash")


pay(context_credit_card, 100)  # Pay 100 with credit card
pay(context_debit_card, 200)  # Pay 200 with debit card
pay(context_paypal, 300)  # Pay 300 with PayPal
pay(context_cash, 400)  # Pay 400 with cash
