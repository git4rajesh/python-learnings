from Design_Patterns.Behavioural.Chain_Of_Responsibility.atm import ATM


class Client:
    def __init__(self):
        self.atm = ATM()


if __name__ == '__main__':
    client = Client()
    # client.atm.get_amount(525)

    # client.atm.get_amount(475)

    client.atm.get_amount(317)
