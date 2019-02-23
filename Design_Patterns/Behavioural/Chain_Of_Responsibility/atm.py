from Design_Patterns.Behavioural.Chain_Of_Responsibility.parent_amount_handler import \
    Child_Amount_Hundred_Handler

from Design_Patterns.Behavioural.Chain_Of_Responsibility.parent_amount_handler import \
    Child_Amount_Fifty_Handler

from Design_Patterns.Behavioural.Chain_Of_Responsibility.parent_amount_handler import \
    Child_Amount_Twenty_Handler

from Design_Patterns.Behavioural.Chain_Of_Responsibility.parent_amount_handler import \
    Child_Amount_Five_Handler


class ATM:
    def __init__(self):
        self.hundred_handler = Child_Amount_Hundred_Handler()
        self.fifty_handler = Child_Amount_Fifty_Handler()
        self.twenty_handler = Child_Amount_Twenty_Handler()
        self.five_handler = Child_Amount_Five_Handler()

        self.hundred_handler.next_amt_handler(self.fifty_handler)
        self.fifty_handler.next_amt_handler(self.twenty_handler)
        self.twenty_handler.next_amt_handler(self.five_handler)

    def get_amount(self, amount):
        print('Amount requested is %s' % amount)
        self.hundred_handler.dispatch_amt(amount)
