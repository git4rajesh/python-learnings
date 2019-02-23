from abc import abstractmethod


class Parent_Amount_Handler:
    @abstractmethod
    def dispatch_amt(self, amount):
        pass

    def next_amt_handler(self, amt_handler):
        self.next_amt_handler = amt_handler


class Child_Amount_Hundred_Handler(Parent_Amount_Handler):
    def dispatch_amt(self, amount):
        if amount > 100:
            print('Dispatched %s notes/note from Hundred Handler' % int(amount / 100))
            pending_amt = (amount % 100)
        else:
            pending_amt = amount

        self.next_amt_handler.dispatch_amt(pending_amt)


class Child_Amount_Fifty_Handler(Parent_Amount_Handler):
    def dispatch_amt(self, amount):
        if amount > 50:
            print('Dispatched %s notes/note from Fifty Handler' % int(amount / 50))
            pending_amt = (amount % 50)
        else:
            pending_amt = amount

        self.next_amt_handler.dispatch_amt(pending_amt)


class Child_Amount_Twenty_Handler(Parent_Amount_Handler):
    def dispatch_amt(self, amount):
        if amount > 20:
            print('Dispatched %s notes/note from Twenty Handler' % int(amount / 20))
            pending_amt = (amount % 20)
        else:
            pending_amt = amount

        self.next_amt_handler.dispatch_amt(pending_amt)


class Child_Amount_Five_Handler(Parent_Amount_Handler):
    def dispatch_amt(self, amount):
        if amount >= 5:
            print('Dispatched %s notes/note from Five Handler' % int(amount / 5))
            pending_amt = (amount % 5)
        else:
            pending_amt = amount

        print('Dispatch completed !!!')
        print('Pending amount is {}'.format(pending_amt))

        if pending_amt:
            print('ATM Doesnt support this denomination. Think that U r contributing to GST!!!!')
