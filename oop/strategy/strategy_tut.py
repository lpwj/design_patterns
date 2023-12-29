from abc import ABC, abstractmethod


# Strategy interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete strategies
class CreditCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with credit card (Strategy Pattern)")


class DebitCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with debit card (Strategy Pattern)")


class PayPal(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with PayPal (Strategy Pattern)")


class Cash(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with cash (Strategy Pattern)")


# Context class
class PaymentContext:
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
