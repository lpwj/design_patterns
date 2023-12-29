from factory_base import PaymentContext

# Example usage
context_credit_card = PaymentContext("CreditCard")
context_debit_card = PaymentContext("DebitCard")
context_paypal = PaymentContext("PayPal")
context_cash = PaymentContext("Cash")

context_credit_card.pay(100)  # Pay 100 with credit card
context_debit_card.pay(200)  # Pay 200 with debit card

context_paypal.pay(300)  # Pay 300 with PayPal
context_cash.pay(400)  # Pay 400 with cash

context_credit_card.pay(200)  # Pay 200 with credit card
context_credit_card.pay(300)  # Pay 300 with credit card
