from abc import ABC, abstractmethod


# Product interface
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# Concrete products
class CreditCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with credit card")


class DebitCard(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with debit card")


class PayPal(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with PayPal")


class Cash(Payment):
    def pay(self, amount: float) -> None:
        print(f"Pay {amount} with cash")


# FACTORIES: dict[str, Payment] = {
#     "CreditCard": CreditCard,
#     "DebitCard": DebitCard,
#     "PayPal": PayPal,
#     "Cash": Cash,
# }


# Factory class
class PaymentFactory:
    def create_payment(self, type: str):
        # return FACTORIES.get(type)()
        if type == "CreditCard":
            return CreditCard()
        elif type == "DebitCard":
            return DebitCard()
        elif type == "PayPal":
            return PayPal()
        elif type == "Cash":
            return Cash()
        else:
            return None


# Context class
class PaymentContext:
    def __init__(self, payment_factory: Payment) -> None:
        self.payment_factory = payment_factory

    def pay(self, type: str, amount: float) -> None:
        payment = self.payment_factory.create_payment(type)
        payment.pay(amount)


# Example usage
factory = PaymentFactory()
context = PaymentContext(factory)
context.pay("CreditCard", 100)  # Pay 100 with credit card
context.pay("DebitCard", 200)  # Pay 200 with debit card
context.pay("PayPal", 300)  # Pay 300 with PayPal
context.pay("Cash", 400)  # Pay 400 with cash
context.pay("CreditCard", 200)  # Pay 200 with credit card
context.pay("CreditCard", 300)  # Pay 300 with credit card
