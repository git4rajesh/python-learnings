class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

# Object Representation: __str__, __repr__
# __repr__: The “official” string representation of an object.
# This is how you would make an object of the class. The goal of __repr__ is to be unambiguous.

# __str__: The “informal” or nicely printable string representation of an object.
# This is for the enduser.

#If you wanted to implement just one of these to-string methods on a Python class,
# make sure it’s __repr__.

    def __repr__(self):
        return '{0} ({1}, {2})'.format(self.__class__.__name__, self.owner, self.amount)

    def __str__(self):
        return '{0} of {1} with starting amount: {2}'.format(
            self.__class__.__name__, self.owner, self.amount)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    # Now I have some data and I want to know:
    # How  many  transactions were there?
    # Index the account object to get transaction number?
    # Loop over the transactions

    # Operator Overloading for Comparing Accounts:

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    # Callable Python Objects: __call__
    # Now when I  call the object with the double-parentheses acc() syntax,
    # I get a nice account statement with an overview of all transactions and the
    # current balance:

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))

    # Context Manager Support and the  With Statement: __enter__, __exit__
    # A context manager is a simple “protocol” (or interface) that
    # your object needs to follow so it can be used with the with statement.
    # Basically all you need to do is add __enter__ and __exit__ methods to an object
    # if you want it to function as a context manager.


if __name__ == '__main__':
    acc = Account('bob')  # default amount = 0
    acc1 = Account('bob', 10)

    acc1.add_transaction(20)
    acc1.add_transaction(-10)
    acc1.add_transaction(50)
    acc1.add_transaction(-20)
    acc1.add_transaction(30)
    print(acc1.balance)
    print(len(acc1))

    for trans in acc1:
        print(trans)

    print(acc > acc1)

    acc1()




