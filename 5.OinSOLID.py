# The Open/Closed Principle states that software entities (classes, functions, modules) 
# should be open for extension but closed for modification.
# This means we should be able to add new functionality without changing existing code.

# Imagine you wrote a payment system. Tomorrow, you want to add a new payment method.
# If you modify existing classes every time, you risk breaking old functionality.
# Instead, by using the Open/Closed Principle, you design the system so new features can be a
# added without touching old code — usually achieved with inheritance or interfaces/abstraction.

class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this methoad")
    
class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f" Paid {amount} using Paypal")

class UPIPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

def complete_payment(payment_method, amount):
    payment_method.pay(amount)

complete_payment(CreditCardPayment(), 1000)
complete_payment(PayPalPayment(), 500)
complete_payment(UPIPayment(), 750)
