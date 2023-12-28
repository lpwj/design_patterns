from abc import ABC, abstractmethod


# Strategy interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete strategies
class CreditCard(Payment):
    def pay(self, amount) -> None:
        print(f"Pay {amount} with credit card")


class DebitCard(Payment):
    def pay(self, amount) -> None:
        print(f"Pay {amount} with debit card")


class PayPal(Payment):
    def pay(self, amount) -> None:
        print(f"Pay {amount} with PayPal")


class Cash(Payment):
    def pay(self, amount) -> None:
        print(f"Pay {amount} with cash")


# Context class
class PaymentContext:
    payment: Payment

    def __init__(self, payment: Payment) -> None:
        self.payment = payment

    def set_payment(self, payment: Payment) -> None:
        self.payment = payment

    def pay(self, amount: float) -> None:
        self.payment.pay(amount)


# Example usage
context = PaymentContext(CreditCard())
context.pay(100)  # Pay 100 with credit card
context.set_payment(DebitCard())
context.pay(200)  # Pay 200 with debit card
context.set_payment(PayPal())
context.pay(300)  # Pay 300 with PayPal
context.set_payment(Cash())
context.pay(400)  # Pay 400 with cash
