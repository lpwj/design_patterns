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
    print(f"Pay {amount} with credit card")


def debit_card(amount: float):
    print(f"Pay {amount} with debit card")


def pay_pal(amount: float):
    print(f"Pay {amount} with PayPal")


def cash(amount: float):
    print(f"Pay {amount} with cash")


# Example usage
pay(credit_card, 100)  # Pay 100 with credit card
pay(debit_card, 200)  # Pay 200 with debit card
pay(pay_pal, 300)  # Pay 300 with PayPal
pay(cash, 400)  # Pay 400 with cash
