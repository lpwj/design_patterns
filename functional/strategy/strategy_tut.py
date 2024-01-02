"""Module with the strategy pattern. (Functional programming)"""
from typing import Callable


def pay(func: Callable[[float], None], amount: float):
    """Executes the action of paying according to the strategy function received.

    Args:
        func (Callable[[float], None]): Function to execute.
        amount (float): The amount to pay.
    """
    func(amount)


# Some concrete functions that represent different payment methods
def credit_card(amount: float):
    """Represents the credit card payment method.

    Args:
        amount (float): The amount to pay.
    """
    print(f"Pay {amount} with credit card (Strategy Functional)")


def debit_card(amount: float):
    """Represents the debit card payment method.

    Args:
        amount (float): The amount to pay.
    """
    print(f"Pay {amount} with debit card (Strategy Functional)")


def paypal(amount: float):
    """Represents the paypal card payment method.

    Args:
        amount (float): The amount to pay.
    """
    print(f"Pay {amount} with PayPal (Strategy Functional)")


def cash(amount: float):
    """Represents the cash payment method.

    Args:
        amount (float): The amount to pay.
    """
    print(f"Pay {amount} with cash (Strategy Functional)")


# Example usage
pay(credit_card, 100)  # Pay 100 with credit card
pay(debit_card, 200)  # Pay 200 with debit card
pay(paypal, 300)  # Pay 300 with PayPal
pay(cash, 400)  # Pay 400 with cash
