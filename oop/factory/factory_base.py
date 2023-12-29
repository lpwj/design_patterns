from abc import ABC, abstractmethod

# from typing import Callable


# Interface of possible factories outcomes
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete factory outcomes
class CreditCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with credit card (Factory Pattern)")


class DebitCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with debit card (Factory Pattern)")


class PayPal(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with PayPal (Factory Pattern)")


class Cash(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with cash (Factory Pattern)")


# FACTORIES: dict[str, Callable[[], Payment]] = {
#     "CreditCard": lambda: CreditCard(),
#     "DebitCard": lambda: DebitCard(),
#     "PayPal": lambda: PayPal(),
#     "Cash": lambda: Cash(),
# }


# Creator class to create the outcome according to the type of factory
class PaymentFactoryCreator:
    outcome: Payment | None

    def __init__(self, type: str) -> None:
        # self.outcome = FACTORIES[type]()
        # return
        if type == "CreditCard":
            self.outcome = CreditCard()
        elif type == "DebitCard":
            self.outcome = DebitCard()
        elif type == "PayPal":
            self.outcome = PayPal()
        elif type == "Cash":
            self.outcome = Cash()
        else:
            self.outcome = None


# Context class to grab the factory type, creates it and the executes the payment.
class PaymentContext:
    payment: Payment
    payment_factory: PaymentFactoryCreator

    def __init__(self, type: str) -> None:
        self.payment_factory = PaymentFactoryCreator(type)

    def pay(self, amount: float) -> None:
        payment = self.payment_factory.outcome
        if payment:
            payment.pay(amount)
