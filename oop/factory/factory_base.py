"""Module with the factory pattern."""
from abc import ABC, abstractmethod

# from typing import Callable


# Interface of possible factories outcomes
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


# Concrete factory outcomes
class CreditCard(Payment):
    """The CreditCard type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with credit card (Factory Pattern)")


class DebitCard(Payment):
    """The DebitCard type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with debit card (Factory Pattern)")


class PayPal(Payment):
    """The PayPal type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with PayPal (Factory Pattern)")


class Cash(Payment):
    """The Cash type of payment blueprint definition.

    Args:
        Payment (ABC): The payment Abstract class.
    """

    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with cash (Factory Pattern)")


# FACTORIES: dict[str, Callable[[], Payment]] = {
#     "CreditCard": lambda: CreditCard(),
#     "DebitCard": lambda: DebitCard(),
#     "PayPal": lambda: PayPal(),
#     "Cash": lambda: Cash(),
# }


class PaymentFactoryCreator:
    """Creator class to create the outcome according to the type of factory"""

    outcome: Payment | None

    def __init__(self, payment_type: str) -> None:
        # self.outcome = FACTORIES[type]()
        # return
        if payment_type == "CreditCard":
            self.outcome = CreditCard()
        elif payment_type == "DebitCard":
            self.outcome = DebitCard()
        elif payment_type == "PayPal":
            self.outcome = PayPal()
        elif payment_type == "Cash":
            self.outcome = Cash()
        else:
            self.outcome = None


class PaymentContext:
    """Context class to grab the factory type, creates it and the executes the payment."""

    payment: Payment
    payment_factory: PaymentFactoryCreator

    def __init__(self, payment_type: str) -> None:
        self.payment_factory = PaymentFactoryCreator(payment_type)

    def pay(self, amount: float) -> None:
        """Performs the actual payment according to the factory outcome in usage.

        Args:
            amount (float): The amount to pay.
        """
        payment = self.payment_factory.outcome
        if payment:
            payment.pay(amount)
