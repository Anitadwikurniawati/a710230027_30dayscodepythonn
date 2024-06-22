class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        if payment_method == "credit_card":
            self.process_credit_card_payment(amount)
        elif payment_method == "paypal":
            self.process_paypal_payment(amount)

    def process_credit_card_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

    def process_paypal_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

processor = PaymentProcessor()
processor.process_payment("credit_card", 100)
processor.process_payment("paypal", 200)
