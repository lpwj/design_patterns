"""Module with the strategy pattern."""
from abc import ABC, abstractmethod


# Strategy interface
class Payment(ABC):
    """Payments Abstract Class

    Args:
        ABC (ABC): Python Base ABC class
    """

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Pay method to be implemented on each class that inherits from this class

        Args:
            amount (float): The amount to pay.
        """


# Concrete strategies
class CreditCard(Payment):
    """The CreditCard type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with credit card (Strategy Pattern)")


class DebitCard(Payment):
    """The DebitCard type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with debit card (Strategy Pattern)")


class PayPal(Payment):
    """The PayPal type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with PayPal (Strategy Pattern)")


class Cash(Payment):
    """The Cash type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with cash (Strategy Pattern)")


# Context class
class PaymentContext:
    """The context class to init or set a new strategy and perform a payment."""

    payment_strategy: Payment

    def __init__(self, payment_strategy: Payment) -> None:
        """Sets the initial payment strategy to use.

        Args:
            payment_strategy (Payment): The payment strategy.
        """
        self.payment_strategy = payment_strategy

    def set_payment(self, payment_strategy: Payment) -> None:
        """Changes the object behavior in run time, and applies a new strategy.

        Args:
            payment_strategy (Payment): The new payment strategy.
        """
        self.payment_strategy = payment_strategy

    def pay(self, amount: float) -> None:
        """Performs the actual payment according to the strategy in usage.

        Args:
            amount (float): The amount to pay.
        """
        self.payment_strategy.pay(amount)


# Example usage
context = PaymentContext(CreditCard())
context.pay(100)  # Pay 100 with credit card

context.set_payment(DebitCard())
context.pay(200)  # Pay 200 with debit card

context.set_payment(PayPal())
context.pay(300)  # Pay 300 with PayPal

context.set_payment(Cash())
context.pay(400)  # Pay 400 with cash
